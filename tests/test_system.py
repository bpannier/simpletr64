import unittest

import defaults
from simpletr64.actions.system import System
from simpletr64.devicetr64 import DeviceTR64


class TestSystem(unittest.TestCase):

    def test_SystemInfo(self):
        box = System(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        sysInfo = box.getSystemInfo()

        self.assertTrue(sysInfo.manufactureName)
        self.assertTrue(sysInfo.modelName)
        self.assertTrue(sysInfo.description)
        self.assertTrue(sysInfo.serialNumber)
        self.assertTrue(sysInfo.softwareVersion)
        self.assertTrue(sysInfo.hwVersion)
        self.assertTrue(sysInfo.uptime >= 0)
        self.assertTrue(sysInfo.log)
        self.assertTrue(len(sysInfo.raw.keys()) > 0)

    def test_TimeInfo(self):
        box = System(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        timeInfo = box.getTimeInfo()

        self.assertTrue(timeInfo.ntpServer1)
        # self.assertTrue(timeInfo.ntpServer2)
        self.assertTrue(timeInfo.currentLocalTime)
        # self.assertTrue(timeInfo.localTimeZone)
        self.assertTrue(timeInfo.localTimeZoneName)
        self.assertTrue(timeInfo.isDaylightSaving is not None)
        self.assertTrue(timeInfo.daylightSavingStart is not None)
        self.assertTrue(timeInfo.daylightSavingEnd)
        self.assertTrue(len(timeInfo.raw.keys()) > 0)
