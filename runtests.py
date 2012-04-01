#!/usr/bin/env python
#
#  Copyright (c) 2011-2012 Corey Goldberg (http://goldb.org)
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


""" run unit tests for linux-metrics """



import sys
import unittest



try:
    from linux_metrics import cpu_stat
    from linux_metrics import cpu_stat_tests
    
    from linux_metrics import disk_stat
    from linux_metrics import disk_stat_tests
    
    from linux_metrics import mem_stat
    from linux_metrics import mem_stat_tests
    
    from linux_metrics import net_stat
    from linux_metrics import net_stat_tests
except ImportError as e:
    print e
    print 'aborting tests'
    sys.exit(1)




if __name__ == '__main__':
    # for each module, there is a <module>_tests.py
    # module containing unittest classes.
    # they are referrenced and loaded below.
    test_cases = [
        cpu_stat_tests.TestCPUStats, 
        disk_stat_tests.TestDiskStats,
        mem_stat_tests.TestMemoryStats,
        net_stat_tests.TestNetworkStats,
    ]    
    test_suites = [
        unittest.TestLoader().loadTestsFromTestCase(test_case)
            for test_case in test_cases
        ]
    all_tests = unittest.TestSuite(test_suites)
    
    # run the tests
    unittest.TextTestRunner(verbosity=2).run(all_tests)
