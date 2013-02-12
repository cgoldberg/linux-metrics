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


from . import mem_stat

import unittest


class TestMemoryStats(unittest.TestCase):
    
    def setUp(self):
        (self.mem_active,
        self.mem_total,
        self.mem_cached,
        self.mem_free,
        self.swap_total,
        self.swap_free) = mem_stat.mem_stats()

    def test_mem_active(self):
        self.assertTrue(self.mem_active > 0)
        
    def test_mem_total(self):
        self.assertTrue(self.mem_total > 0)
        
    def test_mem_cached(self):
        self.assertTrue(self.mem_cached > 0)
        
    def test_mem_free(self):
        self.assertTrue(self.mem_free > 0)

    def test_swap_total(self):
        self.assertTrue(self.swap_total > 0)

    def test_swap_free(self):
        self.assertTrue(self.swap_free > 0)


if __name__ == '__main__':  
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMemoryStats)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
