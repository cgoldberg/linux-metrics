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


from . import disk_stat

import unittest


# configuration
DISK_DEVICE = 'sda1'


class TestDiskStats(unittest.TestCase):
    
    def setUp(self):
        self.device = DISK_DEVICE
        self.sample_duration = .1  # secs
    
    def test_disk_busy(self):
        value = disk_stat.disk_busy(
            self.device,
            self.sample_duration
        )
        self.assertTrue(0.0 <= value <= 100.0, value)
        
    def test_disk_reads(self):
        value, _ = disk_stat.disk_reads_writes(
            self.device
        )
        self.assertTrue(value >= 0, value)
    
    def test_disk_reads_persec(self):
        value, _ = disk_stat.disk_reads_writes_persec(
            self.device,
            self.sample_duration
        )
        self.assertTrue(value >= 0.0, value)
        
    def test_disk_writes(self):
        _, value = disk_stat.disk_reads_writes(
            self.device
        )
        self.assertTrue(value >= 0, value)
        
    def test_disk_writes_persec(self):
        _, value = disk_stat.disk_reads_writes_persec(
            self.device,
            self.sample_duration
        )
        self.assertTrue(value >= 0.0, value)
        
    def test_invalid_disk_interface(self):
        self.assertRaises(
            disk_stat.DiskError,
            disk_stat.disk_busy,
            'invalid_device',
            0
        )



if __name__ == '__main__':  
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestDiskStats)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
