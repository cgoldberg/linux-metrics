#!/usr/bin/env python
#
#  Copyright (c) 2010-2013 Corey Goldberg (http://goldb.org)
#
#  This file is part of linux-metrics
#
#  License :: OSI Approved :: MIT License:
#      http://www.opensource.org/licenses/mit-license
# 
#      Permission is hereby granted, free of charge, to any person obtaining a copy
#      of this software and associated documentation files (the "Software"), to deal
#      in the Software without restriction, including without limitation the rights
#      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#      copies of the Software, and to permit persons to whom the Software is
#      furnished to do so, subject to the following conditions:
#
#      The above copyright notice and this permission notice shall be included in
#      all copies or substantial portions of the Software.
#


"""
    cpu_stat - Python Module for CPU Stats on Linux
    
    
    requires:
    - Python 2.6+
    - Linux 2.6+

"""


import time



def cpu_times():
    """Return a sequence of cpu times.

    each number in the sequence is the amount of time, measured in units 
    of USER_HZ (1/100ths of a second on most architectures), that the system
    spent in each cpu mode: 
    (user, nice, system, idle, iowait, irq, softirq, [steal], [guest]).
    
    on SMP systems, these are aggregates of all processors/cores.
    """
    
    with open('/proc/stat') as f:
        line = f.readline()
    
    cpu_times = [int(x) for x in line.split()[1:]]
    
    return cpu_times
    
    
    
def cpu_percents(sample_duration=1):
    """Return a dictionary of usage percentages and cpu modes.
    
    elapsed cpu time samples taken at 'sample_time (seconds)' apart.
    
    cpu modes: 'user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq'
    
    on SMP systems, these are aggregates of all processors/cores.
    """
    
    deltas = __cpu_time_deltas(sample_duration)
    total = sum(deltas)
    percents = [100 - (100 * (float(total - x) / total)) for x in deltas]

    return {
        'user': percents[0],
        'nice': percents[1],
        'system': percents[2],
        'idle': percents[3],
        'iowait': percents[4],
        'irq': percents[5],
        'softirq': percents[6],
    }



def procs_running():
    """Return number of processes in runnable state."""
    
    return __proc_stat('procs_running')



def procs_blocked():
    """Return number of processes blocked waiting for I/O to complete."""
    
    return __proc_stat('procs_blocked')
    


def file_desc():
    """Return tuple with the number of allocated file descriptors,
    allocated free file descriptors, and max allowed open file descriptors.
    
    The number of file descriptors in use can be calculated as follows:
    
        fd = file_desc()
        in_use = fd[0] - fd[1]
    """
    
    with open('/proc/sys/fs/file-nr') as f:
        line = f.readline()
    
    fd = [int(x) for x in line.split()]
    
    return fd



def load_avg():
    """Return a sequence of system load averages (1min, 5min, 15min)."""
    
    with open('/proc/loadavg') as f:
        line = f.readline()
    
    load_avgs = [float(x) for x in line.split()[:3]]
    
    return load_avgs
        


def cpu_info():
    """Return the logical cpu info. On SMP systems, the values are
    representing a single processor. The key processor_count has the number
    of processors.
    """
    
    with open('/proc/cpuinfo') as f:
        cpuinfo = {'processor_count': 0}
        for line in f:
            if ':' in line:
                fields = line.replace('\t', '').strip().split(': ')
                # count processores and filter out core specific items
                if fields[0] == 'processor':
                    cpuinfo['processor_count'] += 1
                elif fields[0] != 'core id':
                    try:
                        cpuinfo[fields[0]] = fields[1]
                    except IndexError:
                        pass
        return cpuinfo



def __cpu_time_deltas(sample_duration):
    """Return a sequence of cpu time deltas for a sample period.
    
    elapsed cpu time samples taken at 'sample_time (seconds)' apart.
    
    each value in the sequence is the amount of time, measured in units 
    of USER_HZ (1/100ths of a second on most architectures), that the system
    spent in each cpu mode: (user, nice, system, idle, iowait, irq, softirq, [steal], [guest]).
    
    on SMP systems, these are aggregates of all processors/cores.
    """
    
    with open('/proc/stat') as f1:
        with open('/proc/stat') as f2:
            line1 = f1.readline()
            time.sleep(sample_duration)
            line2 = f2.readline()
    
    deltas = [int(b) - int(a) for a, b in zip(line1.split()[1:], line2.split()[1:])]
    
    return deltas
    
    
    
def __proc_stat(stat):
    with open('/proc/stat') as f:
        for line in f:
            if line.startswith(stat):
                return int(line.split()[1])
