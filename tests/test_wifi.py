import unittest

import defaults
from simpletr64.actions.wifi import Wifi
from simpletr64.devicetr64 import DeviceTR64


class TestWifi(unittest.TestCase):

    def test_WifiInfo(self):
        box = Wifi(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        wifiInfo = box.getWifiInfo(1)

        self.assertTrue(wifiInfo.enabled or not wifiInfo.enabled)
        self.assertTrue(wifiInfo.status)
        self.assertTrue(wifiInfo.channel > 0)
        self.assertTrue(wifiInfo.ssid)
        self.assertTrue(wifiInfo.bssid)
        self.assertTrue(wifiInfo.beaconType)
        self.assertTrue(wifiInfo.macControl)
        self.assertTrue(wifiInfo.standard)
        self.assertTrue(wifiInfo.encryptionMode)
        self.assertTrue(wifiInfo.authMode)
        self.assertTrue(len(wifiInfo.raw.keys()) > 0)

    def test_WifiStatistic(self):
        box = Wifi(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        stats = box.getStatistic(1)

        self.assertTrue(stats[0] >= 0)
        self.assertTrue(stats[1] >= 0)

    def test_WifiPacketStatistic(self):
        box = Wifi(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        stats = box.getPacketStatistic(1)

        self.assertTrue(stats[0] >= 0)
        self.assertTrue(stats[1] >= 0)

    def test_WifiDeviceInfo(self):
        box = Wifi(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        amount = box.getTotalAssociations(1)
        self.assertTrue(amount > 0, "Amount " + str(amount))

        # get first device in the list on the first wifi interface
        deviceInfo = box.getGenericAssociatedDeviceInfo(0 ,1)

        self.assertTrue(deviceInfo.macAddress)
        self.assertTrue(deviceInfo.ipAddress)
        self.assertTrue(deviceInfo.authenticated)
        self.assertTrue(len(deviceInfo.raw.keys()) > 0)
