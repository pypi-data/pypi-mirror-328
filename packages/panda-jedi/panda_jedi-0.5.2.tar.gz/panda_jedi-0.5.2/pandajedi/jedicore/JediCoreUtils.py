import copy
import datetime
import math
import os
import re

from pandaserver.taskbuffer import JobUtils


# get effective file size
def getEffectiveFileSize(fsize, startEvent, endEvent, nEvents):
    inMB = 1024 * 1024
    if fsize in [None, 0]:
        # use dummy size for pseudo input
        effectiveFsize = inMB
    elif nEvents is not None and startEvent is not None and endEvent is not None:
        # take event range into account
        effectiveFsize = int(float(fsize) * float(endEvent - startEvent + 1) / float(nEvents))
    else:
        effectiveFsize = fsize
    # use dummy size if input is too small
    if effectiveFsize == 0:
        effectiveFsize = inMB
    # in MB
    effectiveFsize = float(effectiveFsize) / inMB
    # return
    return effectiveFsize


# get effective number of events
def getEffectiveNumEvents(startEvent, endEvent, nEvents):
    if endEvent is not None and startEvent is not None:
        evtCounts = endEvent - startEvent + 1
        if evtCounts > 0:
            return evtCounts
        return 1
    if nEvents is not None:
        return nEvents
    return 1


# get memory usage
def getMemoryUsage():
    try:
        t = open(f"/proc/{os.getpid()}/status")
        v = t.read()
        t.close()
        value = 0
        for line in v.split("\n"):
            if line.startswith("VmRSS"):
                items = line.split()
                value = int(items[1])
                if items[2] in ["kB", "KB"]:
                    value /= 1024
                elif items[2] in ["mB", "MB"]:
                    pass
                break
        return int(value)
    except Exception:
        return None


# check process
def checkProcess(pid):
    return os.path.exists(f"/proc/{pid}/status")


# offset for walltime
wallTimeOffset = 10 * 60


# convert config parameters
def convert_config_params(itemStr):
    items = itemStr.split(":")
    newItems = []
    for item in items:
        if item == "":
            newItems.append(None)
        elif "," in item:
            newItems.append(item.split(","))
        else:
            try:
                newItems.append(int(item))
            except Exception:
                newItems.append(item)
    return newItems


# parse init params
def parse_init_params(par):
    if isinstance(par, list):
        return par
    try:
        return par.split("|")
    except Exception:
        return [par]


# get config param for vo and prodSourceLabel
def getConfigParam(configStr, vo, sourceLabel):
    try:
        for _ in configStr.split(","):
            items = configStr.split(":")
            vos = items[0].split("|")
            sourceLabels = items[1].split("|")
            if vo not in ["", "any"] and vo not in vos and None not in vos and "any" not in vos and "" not in vos:
                continue
            if (
                sourceLabel not in ["", "any"]
                and sourceLabel not in sourceLabels
                and None not in sourceLabels
                and "any" not in sourceLabels
                and "" not in sourceLabels
            ):
                continue
            return ",".join(items[2:])
    except Exception:
        pass
    return None


# get percentile until numpy 1.5.X becomes available
def percentile(inList, percent, idMap):
    inList = sorted(copy.copy(inList))
    k = (len(inList) - 1) * float(percent) / 100
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        retVal = inList[int(f)]
        return retVal, [retVal]
    val0 = inList[int(f)]
    val1 = inList[int(c)]
    d0 = val0 * (c - k)
    d1 = val1 * (k - f)
    retVal = d0 + d1
    return retVal, [val0, val1]


# get min ram count for job
def getJobMinRamCount(taskSpec, inputChunk, siteSpec, coreCount):
    minRamCount = inputChunk.getMaxRamCount()
    if inputChunk.isMerging:
        minRamUnit = "MB"
    else:
        minRamUnit = taskSpec.ramUnit
        if minRamUnit in [None, "", "NULL"]:
            minRamUnit = "MB"
        if taskSpec.ramPerCore():
            minRamCount *= coreCount
            minRamCount += taskSpec.baseRamCount
            minRamUnit = re.sub("PerCore.*$", "", minRamUnit)
    # round up with chunks
    minRamCount = JobUtils.compensate_ram_count(minRamCount)
    return minRamCount, minRamUnit


# get max walltime and cpu count
def getJobMaxWalltime(taskSpec, inputChunk, totalMasterEvents, jobSpec, siteSpec):
    try:
        if taskSpec.getCpuTime() is None:
            # use PQ maxtime when CPU time is not defined
            jobSpec.maxWalltime = siteSpec.maxtime
            jobSpec.maxCpuCount = siteSpec.maxtime
        else:
            jobSpec.maxWalltime = taskSpec.getCpuTime()
            if jobSpec.maxWalltime is not None and jobSpec.maxWalltime > 0:
                jobSpec.maxWalltime *= totalMasterEvents
                if siteSpec.coreCount > 0:
                    jobSpec.maxWalltime /= float(siteSpec.coreCount)
                if siteSpec.corepower not in [0, None]:
                    jobSpec.maxWalltime /= siteSpec.corepower
            if taskSpec.cpuEfficiency not in [None, 0]:
                jobSpec.maxWalltime /= float(taskSpec.cpuEfficiency) / 100.0
            if taskSpec.baseWalltime is not None:
                jobSpec.maxWalltime += taskSpec.baseWalltime
            jobSpec.maxWalltime = int(jobSpec.maxWalltime)
            if taskSpec.useHS06():
                jobSpec.maxCpuCount = jobSpec.maxWalltime
    except Exception:
        pass


# use direct IO for job
def use_direct_io_for_job(task_spec, site_spec, input_chunk):
    # not for merging
    if input_chunk and input_chunk.isMerging:
        return False
    # always
    if site_spec.always_use_direct_io():
        return True
    # force copy-to-scratch
    if task_spec.useLocalIO():
        return False
    # depends on task and site specs
    if task_spec.allowInputLAN() is not None and site_spec.isDirectIO():
        return True
    return False


# stopwatch
class StopWatch:
    """Utility class to measure timing information."""

    def __init__(self, identifier: str = None):
        self.start_time = datetime.datetime.now()
        self.checkpoint = self.start_time
        self.step_name = None
        self.identifier = identifier

    def reset(self):
        """Reset the stopwatch."""
        self.start_time = datetime.datetime.now()
        self.checkpoint = self.start_time
        self.step_name = None

    def get_elapsed_time(self, new_step_name: str) -> str:
        """Get the elapsed time since the stopwatch was started and the duration since the last checkpoint.
        :param new_step_name: The name of the next step.
        Returns:
            str: A string with the elapsed time and the duration since the last checkpoint.
        """
        now = datetime.datetime.now()
        total_delta = now - self.start_time
        duration_delta = now - self.checkpoint
        return_str = ""
        if self.identifier:
            return_str += f"{self.identifier}: "
        return_str += f"elapsed {total_delta.seconds}.{int(total_delta.microseconds / 1000):03d} sec. "
        if self.step_name is not None:
            return_str += f"{self.step_name} took {duration_delta.seconds}.{int(duration_delta.microseconds / 1000):03d} sec. "
        if new_step_name:
            return_str += f"{new_step_name} started."
        else:
            return_str += "done."
        self.checkpoint = now
        self.step_name = new_step_name
        return return_str
