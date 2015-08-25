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
    disk_stat - Python Module for Disk Stats on Linux
    
    
    requires:
    - Python 2.6+
    - Linux 2.6+
    
"""


import time
from subprocess import Popen, PIPE

   
def disk_busy(device, sample_duration=1):
    """Return disk busy percent."""
    with open('/proc/diskstats') as f1:
        with open('/proc/diskstats') as f2:
            content1 = f1.read()
            time.sleep(sample_duration)
            content2 = f2.read()
    sep = '%s ' % device
    found = False
    for line in content1.splitlines():
        if sep in line:
            found = True
            io_ms1 = line.strip().split(sep)[1].split()[9]
            break
    if not found:
        raise DiskError('device not found: %r' % device)
    for line in content2.splitlines():
        if sep in line:
            io_ms2 = line.strip().split(sep)[1].split()[9]
            break            
    delta = int(io_ms2) - int(io_ms1)
    total = sample_duration * 1000
    return 100 * (float(delta) / total)

def disk_reads_writes(device):
    """Return number of disk (reads, writes)."""
    with open('/proc/diskstats') as f:
        content = f.read()
    sep = '%s ' % device
    found = False
    for line in content.splitlines():
        if sep in line:
            found = True
            fields = line.strip().split(sep)[1].split()
            num_reads = int(fields[0])
            num_writes = int(fields[4])
            break
    if not found:
        raise DiskError('device not found: %r' % device)
    return (num_reads, num_writes)


def disk_usage(path):
    """Return disk usage statistics about the given path."""    	
    output = Popen(['df', '-k', path], stdout=PIPE).communicate()[0]
    try:
        df = output.splitlines()[2].split()
        device = output.splitlines()[1]
        (size, used, free, percent, mountpoint) = df
    except IndexError:
        df = output.splitlines()[1].split()
        (device, size, used, free, percent, mountpoint) = df
    return (device, int(size), int(used), int(free), percent, mountpoint)


def disk_reads_writes_persec(device, sample_duration=1):
    """Return number of disk (reads, writes) per sec during the sample_duration."""
    with open('/proc/diskstats') as f1:
        with open('/proc/diskstats') as f2:
            content1 = f1.read()
            time.sleep(sample_duration)
            content2 = f2.read()
    sep = '%s ' % device
    found = False
    for line in content1.splitlines():
        if sep in line:
            found = True
            fields = line.strip().split(sep)[1].split()
            num_reads1 = int(fields[0])
            num_writes1 = int(fields[4])
            break
    if not found:
        raise DiskError('device not found: %r' % device)
    for line in content2.splitlines():
        if sep in line:
            fields = line.strip().split(sep)[1].split()
            num_reads2 = int(fields[0])
            num_writes2 = int(fields[4])
            break            
    reads_per_sec = (num_reads2 - num_reads1) / float(sample_duration)
    writes_per_sec = (num_writes2 - num_writes1) / float(sample_duration)   
    return (reads_per_sec, writes_per_sec)



class DiskError(Exception):
    pass
