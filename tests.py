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


""" unit tests for linux-metrics """



import sys
import unittest

try:
    from linux_metrics import cpu_stat
    from linux_metrics import disk_stat
    from linux_metrics import mem_stat
    from linux_metrics import net_stat
except ImportError as e:
    print e
    print 'aborting tests'
    sys.exit(1)
    


# configuration  
DISK_DEVICE = 'sda'
NETWORK_INTERFACE = 'eth0'



def main():
    test_cases = [
        TestCPUStats, 
        TestDiskStats,
        TestMemoryStats,
        TestNetworkStats,
    ]
        
    test_suites = [unittest.TestLoader().loadTestsFromTestCase(test_case) for test_case in test_cases]
    all_tests = unittest.TestSuite(test_suites)
    unittest.TextTestRunner(verbosity=2).run(all_tests)
    
    
    
class TestCPUStats(unittest.TestCase):
    
    def setUp(self):
        self.sample_duration = .1  # secs
        
    def test_cpu_info(self):
        values = cpu_stat.cpu_info()
        self.assertTrue(len(values) > 0, values)
        
    def test_cpu_percent_idle(self):
        value = cpu_stat.cpu_percents(self.sample_duration)['idle']
        self.assertTrue(0.0 <= value <= 100.0, value)
    
    def test_cpu_percent_iowait(self):
        value = cpu_stat.cpu_percents(self.sample_duration)['iowait']
        self.assertTrue(0.0 <= value <= 100.0, value)
    
    def test_cpu_percent_irq(self):
        value = cpu_stat.cpu_percents(self.sample_duration)['irq']
        self.assertTrue(0.0 <= value <= 100.0, value)
    
    def test_cpu_percent_nice(self):
        value = cpu_stat.cpu_percents(self.sample_duration)['nice']
        self.assertTrue(0.0 <= value <= 100.0, value)
        
    def test_cpu_percent_softirq(self):
        value = cpu_stat.cpu_percents(self.sample_duration)['softirq']
        self.assertTrue(0.0 <= value <= 100.0, value)
    
    def test_cpu_percent_system(self):
        value = cpu_stat.cpu_percents(self.sample_duration)['system']
        self.assertTrue(0.0 <= value <= 100.0, value)
        
    def test_cpu_percent_user(self):
        value = cpu_stat.cpu_percents(self.sample_duration)['user']
        self.assertTrue(0.0 <= value <= 100.0, value)
    
    def test_cpu_percents(self):
        values = cpu_stat.cpu_percents(self.sample_duration)
        self.assertTrue(len(values) == 7, values)
        
    def test_cpu_times(self):
        values = cpu_stat.cpu_times()
        self.assertTrue(len(values) >= 7, values)
        
    def test_procs_blocked(self):
        value = cpu_stat.procs_blocked()
        self.assertTrue(value >= 0, value)
        
    def test_procs_running(self):
        value = cpu_stat.procs_running()
        self.assertTrue(value >= 0, value)
        
    def test_load_avg(self):
        values = cpu_stat.load_avg()
        self.assertTrue(len(values) == 3, values)
        
    

class TestDiskStats(unittest.TestCase):
    
    def setUp(self):
        self.device = DISK_DEVICE
        self.sample_duration = .1  # secs
    
    def test_disk_busy(self):
        value = disk_stat.disk_busy(self.device, self.sample_duration)
        self.assertTrue(0.0 <= value <= 100.0, value)
        
    def test_disk_reads(self):
        value, _ = disk_stat.disk_reads_writes(self.device)
        self.assertTrue(value >= 0, value)
    
    def test_disk_reads_persec(self):
        value, _ = disk_stat.disk_reads_writes_persec(self.device, self.sample_duration)
        self.assertTrue(value >= 0.0, value)
        
    def test_disk_writes(self):
        _, value = disk_stat.disk_reads_writes(self.device)
        self.assertTrue(value >= 0, value)
        
    def test_disk_writes_persec(self):
        _, value = disk_stat.disk_reads_writes_persec(self.device, self.sample_duration)
        self.assertTrue(value >= 0.0, value)
        


class TestMemoryStats(unittest.TestCase):
    
    def test_mem_used(self):
        value, _ = mem_stat.mem_stats()
        self.assertTrue(value > 0, value)
        
    def test_mem_total(self):
        _, value = mem_stat.mem_stats()
        self.assertTrue(value > 0, value)



class TestNetworkStats(unittest.TestCase):
    
    def setUp(self):
        self.interface = NETWORK_INTERFACE
        
    def test_rx_bytes(self):
        value, _ = net_stat.rx_tx_bytes(self.interface)
        self.assertTrue(value >= 0, value)
        
    def test_tx_bytes(self):
        _, value = net_stat.rx_tx_bytes(self.interface)
        self.assertTrue(value >= 0, value)
   
    def test_rx_bits(self):
        value, _ = net_stat.rx_tx_bits(self.interface)
        self.assertTrue(value >= 0, value)
        
    def test_tx_bits(self):
        _, value = net_stat.rx_tx_bits(self.interface)
        self.assertTrue(value >= 0, value)



if __name__ == '__main__':
    main()
    
