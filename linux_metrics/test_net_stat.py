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


from . import net_stat

import unittest


# configuration
NETWORK_INTERFACE = 'eth0'


class TestNetworkStats(unittest.TestCase):
    
    def setUp(self):
        self.interface = NETWORK_INTERFACE

    def test_rx_tx_bytes(self):
        rx, tx = net_stat.rx_tx_bytes(
            self.interface
        )
        self.assertTrue(rx >= 0, rx)
        self.assertTrue(tx >= 0, tx)

    def test_rx_tx_bits(self):
        rx, tx = net_stat.rx_tx_bits(
            self.interface
        )
        self.assertTrue(rx >= 0, rx)
        self.assertTrue(tx >= 0, tx)
        
    def test_rx_tx_dump(self):
        rx, tx = net_stat.rx_tx_bits(
            self.interface
        )
        rx, tx = map(int, (rx, tx))
        self.assertTrue(rx >= 0, rx)
        self.assertTrue(tx >= 0, tx)

    def test_invalid_net_interface(self):
        self.assertRaises(
            net_stat.NetError,
            net_stat.rx_tx_bytes, 
            'eth-BAD'
        )



if __name__ == '__main__':  
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestNetworkStats)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
