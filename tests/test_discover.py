import unittest

import defaults
from simpletr64.devicetr64 import DeviceTR64
from simpletr64.discover import Discover


class TestDiscover(unittest.TestCase):

    def test_discover(self):
        results = Discover.discover(retries=1)
        self.assertTrue(len(results) > 0)

    def test_InitalizeSCPD(self):
        results = Discover.discover(retries=2)
        self.assertTrue(len(results) > 0, "No UPnP host found at all.")

        # setup proxies for discovery call
        proxies = {}
        if defaults.test_httpsProxy:
            proxies = {"https": defaults.test_httpsProxy}

        if defaults.test_httpProxy:
            proxies = {"http": defaults.test_httpProxy}

        # pick the best device in the result list for later loads
        bestResult = None
        for result in results:
            if Discover.rateServiceTypeInResult(result) > Discover.rateServiceTypeInResult(bestResult):
                bestResult = result

        # find the device again
        result = Discover.discoverParticularHost(bestResult.locationHost, proxies=proxies, retries=1)
        self.assertTrue(result is not None, "Failed to discover: " + bestResult.locationHost)

        box = DeviceTR64(result.locationHost, result.locationPort, result.locationProtocol)
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        # the discovery result contains the right URL to initialize device definitions
        box.loadDeviceDefinitions(result.location)
        # load the actions
        box.loadSCPD()

        # the following calls can fail if the device found has not all the definitions needed
        #
        self.assertTrue(len(box.deviceServiceDefinitions.keys()) > 0, "Host: " + result.locationHost +
                        " Result used: " + str(result))
        self.assertTrue(len(box.deviceInformations.keys()) > 0, "Host: " + result.locationHost +
                        " Result used: " + str(result))
        self.assertTrue(len(box.deviceSCPD.keys()) > 0, "Host: " + result.locationHost +
                        " Result used: " + str(result))





