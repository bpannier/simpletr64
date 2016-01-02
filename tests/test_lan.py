import unittest

import defaults
from simpletr64.actions.lan import Lan
from simpletr64.devicetr64 import DeviceTR64


class TestLan(unittest.TestCase):

    def test_AmountOfHostsConnected(self):
        box = DeviceTR64(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        lan = Lan(box)
        amount = lan.getAmountOfHostsConnected()

        self.assertTrue(amount > 0)

    def test_HostDetailsByIndex(self):
        box = DeviceTR64(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        lan = Lan(box)
        hostDetails = lan.getHostDetailsByIndex(0)

        self.assertTrue(hostDetails.ipaddress)
        self.assertTrue(hostDetails.hostname)
        self.assertTrue(hostDetails.macAddress)
        self.assertTrue(hostDetails.interface)
        self.assertTrue(hostDetails.source)
        self.assertTrue(hostDetails.leasetime >= 0)
        self.assertTrue(hostDetails.active or not hostDetails.active)
        self.assertTrue(len(hostDetails.raw.keys()) > 0)

    def test_HostDetailsByMac(self):
        box = DeviceTR64(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        lan = Lan(box)
        hostDetailsForFirst = lan.getHostDetailsByIndex(0)

        hostDetails = lan.getHostDetailsByIndex(hostDetailsForFirst.macAddress)

        self.assertTrue(hostDetails.ipaddress)
        self.assertTrue(hostDetails.hostname)
        self.assertTrue(hostDetails.macAddress)
        self.assertTrue(hostDetails.interface)
        self.assertTrue(hostDetails.source)
        self.assertTrue(hostDetails.leasetime >= 0)
        self.assertTrue(hostDetails.active or not hostDetails.active)
        self.assertTrue(len(hostDetails.raw.keys()) > 0)

    def test_EhternetInfo(self):
        box = DeviceTR64(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        lan = Lan(box)
        ethernetInfo = lan.getEthernetInfo()

        self.assertTrue(ethernetInfo.enabled or not ethernetInfo.enabled)
        self.assertTrue(ethernetInfo.status)
        self.assertTrue(ethernetInfo.macAddress)
        self.assertTrue(ethernetInfo.maxBitRate)
        self.assertTrue(ethernetInfo.duplexMode)
        self.assertTrue(len(ethernetInfo.raw.keys()) > 0)

    def test_EhternetStatistic(self):
        box = DeviceTR64(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        lan = Lan(box)
        ethernetStatistic = lan.getEthernetStatistic()

        self.assertTrue(ethernetStatistic.bytesSent >= 0)
        self.assertTrue(ethernetStatistic.bytesReceived >= 0)
        self.assertTrue(ethernetStatistic.packetsSent >= 0)
        self.assertTrue(ethernetStatistic.packetsReceived >= 0)
        self.assertTrue(len(ethernetStatistic.raw.keys()) > 0)
