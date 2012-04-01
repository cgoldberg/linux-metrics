#!/usr/bin/env python
#
#  Copyright (c) 2010-2012 Corey Goldberg (http://goldb.org)
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


import net_stat
import unittest



# configuration
NETWORK_INTERFACE = 'eth1'



class TestNetworkStats(unittest.TestCase):
    
    def setUp(self):
        self.interface = NETWORK_INTERFACE
        
    def test_rx_bytes(self):
        value, _ = net_stat.rx_tx_bytes(
            self.interface
        )
        self.assertTrue(value >= 0, value)
        
    def test_tx_bytes(self):
        _, value = net_stat.rx_tx_bytes(
            self.interface
        )
        self.assertTrue(value >= 0, value)
   
    def test_rx_bits(self):
        value, _ = net_stat.rx_tx_bits(
            self.interface
        )
        self.assertTrue(value >= 0, value)
        
    def test_tx_bits(self):
        _, value = net_stat.rx_tx_bits(
            self.interface
        )
        self.assertTrue(value >= 0, value)
    
    def test_invalid_net_interface(self):
        self.assertRaises(
            net_stat.NetError,
            net_stat.rx_tx_bytes, 
            'invalid_interface'
        )



if __name__ == '__main__':  
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestNetworkStats)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
