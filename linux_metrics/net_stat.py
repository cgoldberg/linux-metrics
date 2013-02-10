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
    net_stat - Python Module for Network Stats on Linux
    
    
    requires:
    - Python 2.6+
    - Linux 2.6+
    
"""



import re
import subprocess



def rx_tx_bytes(interface):  # by reading /proc
    for line in open('/proc/net/dev'):
        if interface in line:
            data = line.split('%s:' % interface)[1].split()
            rx_bytes, tx_bytes = (int(data[0]), int(data[8]))
            return (rx_bytes, tx_bytes)
    raise NetError('interface not found: %r' % interface)


def rx_tx_bits(interface):  # by reading /proc
    rx_bytes, tx_bytes = rx_tx_bytes(interface)
    rx_bits = rx_bytes * 8
    tx_bits = tx_bytes * 8
    return (rx_bits, tx_bits)
            
def rx_tx_dump(interface): #get all info
	for line in open('/proc/net/dev'):
		if interface in line:
			data = line.split('%s:' % interface)[1].split()
			rx, tx = [int(x) for x in data[0:8]], [int(x) for x in data[8:]]
	return (rx, tx)

def net_stats_ifconfig(interface):  # by parsing ifconfig output   
    output = subprocess.Popen(['ifconfig', interface], stdout=subprocess.PIPE).communicate()[0]
    rx_bytes = int(re.findall('RX bytes:([0-9]*) ', output)[0])
    tx_bytes = int(re.findall('TX bytes:([0-9]*) ', output)[0])
    return (rx_bytes, tx_bytes)
         

class NetError(Exception):
    pass


