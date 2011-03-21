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
    net_stat - Python Module for Network Stats on Linux
    
    
    requires:
    - Python 2.6+
    - Linux 2.6.x
    
"""



import re
import subprocess



def main():
    rx_bytes, tx_bytes = rx_tx_bytes('eth0')
    print '%s bytes received' % rx_bytes
    print '%s bytes sent' % tx_bytes
    
    rx_bits, tx_bits = rx_tx_bits('eth0')
    print '%s bits received' % rx_bits
    print '%s bits sent' % tx_bits 
    
    rx_bytes, tx_bytes = net_stats_ifconfig('eth0')
    print '%s bytes received' % rx_bytes
    print '%s bytes sent' % tx_bytes
    
    

def rx_tx_bytes(interface):  # by reading /proc
    for line in open('/proc/net/dev'):
        if interface in line:
            data = line.split('%s:' % interface)[1].split()
            rx_bytes, tx_bytes = (int(data[0]), int(data[8]))
            return (rx_bytes, tx_bytes)



def rx_tx_bits(interface):  # by reading /proc
    rx_bytes, tx_bytes = rx_tx_bytes(interface)
    rx_bits = rx_bytes * 8
    tx_bits = tx_bytes * 8
    return (rx_bits, tx_bits)
            
            

def net_stats_ifconfig(interface):  # by parsing ifconfig output   
    output = subprocess.Popen(['ifconfig', interface], stdout=subprocess.PIPE).communicate()[0]
    rx_bytes = int(re.findall('RX bytes:([0-9]*) ', output)[0])
    tx_bytes = int(re.findall('TX bytes:([0-9]*) ', output)[0])
    return (rx_bytes, tx_bytes)
         


if __name__ == '__main__':
    main()