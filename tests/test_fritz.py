import unittest

import defaults
from simpletr64.actions.fritz import Fritz


class TestFritz(unittest.TestCase):

    def test_Update(self):
        box = Fritz(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        (updateAvailable, updateStr) = box.doUpdate()

        self.assertTrue(updateStr)

    def test_OptimizedForIPTV(self):
        box = Fritz(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        isOptimized = box.isOptimizedForIPTV()

        box.setOptimizedForIPTV(not isOptimized)
        isOptimized2 = box.isOptimizedForIPTV()

        self.assertEqual(isOptimized2, not isOptimized)

        box.setOptimizedForIPTV(isOptimized)
        isOptimized2 = box.isOptimizedForIPTV()

        self.assertEqual(isOptimized2, isOptimized)

    def test_CallList(self):
        box = Fritz(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        callList = box.getCallList()

        self.assertTrue(len(callList))
