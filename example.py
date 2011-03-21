#!/usr/bin/env python
#
#  Copyright (c) 2011 Corey Goldberg (http://goldb.org)
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


""" example usage of linux-metrics """



from linux_metrics import cpu_stat, disk_stat, mem_stat, net_stat



def main():
    
    # cpu
    print 'procs running: %d' % cpu_stat.procs_running()
    cpu_pcts = cpu_stat.cpu_percents(sample_duration=1)
    print 'cpu utilization: %.2f%%' % (100 - cpu_pcts['idle']) 
    
    # disk
    print 'disk busy: %s%%' % disk_stat.disk_busy('sda', sample_duration=1)
    r, w = disk_stat.disk_reads_writes('sda')    
    print 'disk reads: %s' % r
    print 'disk writes: %s' % w
    
    # memory
    used, total = mem_stat.mem_stats()
    print 'mem used: %s' % used
    print 'mem total: %s' % total

    # network
    rx_bits, tx_bits = net_stat.rx_tx_bits('eth0')   
    print 'net bits received: %s' % rx_bits
    print 'net bits sent: %s' % tx_bits 

    
    
if __name__ == '__main__':   
    main()


