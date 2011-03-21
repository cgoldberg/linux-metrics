#!/usr/bin/env python
#
#  Copyright (c) 2010-2011 Corey Goldberg (http://goldb.org)
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
    - Linux 2.6.x
    
    
    functions:
    - disk_busy(device, sample_duration=1)
    - disk_reads_writes(device)
    - disk_reads_writes_persec(device, sample_duration=1)
    
    
    example:
    
        #!/usr/bin/env python
        
        import disk_stat
        
        r, w = disk_stat.disk_reads_writes('sda')
        print 'reads: %s' % r
        print 'writes: %s' % w
        
        print 'busy: %s%%' % disk_stat.disk_busy('sda', 5)
        
        rps, wps = disk_stat.disk_reads_writes_persec('sda', 5)
        print 'reads per sec: %s' % rps
        print 'writes per sec: %s' % wps
    
"""


import time


   
def disk_busy(device, sample_duration=1):
    """Return disk busy percent."""
    with open('/proc/diskstats') as f1:
        with open('/proc/diskstats') as f2:
            content1 = f1.read()
            time.sleep(sample_duration)
            content2 = f2.read()
    sep = '%s ' % device
    for line in content1.splitlines():
        if sep in line:
            io_ms1 = line.strip().split(sep)[1].split()[9]
            break
    for line in content2.splitlines():
        if sep in line:
            io_ms2 = line.strip().split(sep)[1].split()[9]
            break            
    delta = int(io_ms2) - int(io_ms1)
    total = sample_duration * 1000
    busy_pct = 100 - (100 * (float(total - delta) / total))
    return busy_pct



def disk_reads_writes(device):
    """Return number of disk (reads, writes)."""
    with open('/proc/diskstats') as f:
        content = f.read()
    sep = '%s ' % device
    for line in content.splitlines():
        if sep in line:
            fields = line.strip().split(sep)[1].split()
            num_reads = int(fields[0])
            num_writes = int(fields[4])
            break             
    return num_reads, num_writes
    
    
    
def disk_reads_writes_persec(device, sample_duration=1):
    """Return number of disk (reads, writes) per sec during the sample_duration."""
    with open('/proc/diskstats') as f1:
        with open('/proc/diskstats') as f2:
            content1 = f1.read()
            time.sleep(sample_duration)
            content2 = f2.read()
    sep = '%s ' % device
    for line in content1.splitlines():
        if sep in line:
            fields = line.strip().split(sep)[1].split()
            num_reads1 = int(fields[0])
            num_writes1 = int(fields[4])
            break
    for line in content2.splitlines():
        if sep in line:
            fields = line.strip().split(sep)[1].split()
            num_reads2 = int(fields[0])
            num_writes2 = int(fields[4])
            break            
    reads_per_sec = (num_reads2 - num_reads1) / float(sample_duration)
    writes_per_sec = (num_writes2 - num_writes1) / float(sample_duration)   
    return reads_per_sec, writes_per_sec




if __name__ == '__main__':  
    r, w = disk_reads_writes('sda')
    print 'reads: %s' % r
    print 'writes: %s' % w
    
    print 'busy: %s%%' % disk_busy('sda', 5)
    
    rps, wps = disk_reads_writes_persec('sda', 5)
    print 'reads per sec: %s' % rps
    print 'writes per sec: %s' % wps

