import unittest

import defaults
from simpletr64.actions.wan import Wan
from simpletr64.devicetr64 import DeviceTR64


class TestWan(unittest.TestCase):

    def test_WanLinkInfo(self):
        box = Wan(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        linkInfo = box.getLinkInfo()

        self.assertTrue(linkInfo.enabled or not linkInfo.enabled)
        self.assertTrue(linkInfo.status)
        self.assertTrue(linkInfo.dataPath)
        self.assertTrue(linkInfo.upstreamCurrentRate >= 0)
        self.assertTrue(linkInfo.downStreamCurrentRate >= 0)
        self.assertTrue(linkInfo.upstreamMaxRate >= 0)
        self.assertTrue(linkInfo.downstreamMaxRate >= 0)
        self.assertTrue(len(linkInfo.raw.keys()) > 0)

    def test_WanLinkProperties(self):
        box = Wan(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        linkProperties = box.getLinkProperties()

        self.assertTrue(linkProperties.accessType)
        self.assertTrue(linkProperties.linkStatus)
        self.assertTrue(linkProperties.upstreamMaxBitRate >= 0)
        self.assertTrue(linkProperties.downstreamMaxBitRate >= 0)
        self.assertTrue(len(linkProperties.raw.keys()) > 0)

    def test_ADSLInfo(self):
        box = Wan(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        adslInfo = box.getADSLInfo()

        self.assertTrue(adslInfo.enabled or not adslInfo.enabled)
        self.assertTrue(adslInfo.status)
        self.assertTrue(adslInfo.linkType)
        self.assertTrue(adslInfo.destinationAddress)
        self.assertTrue(len(adslInfo.raw.keys()) > 0)

    def test_EthernetLinkStatus(self):
        box = Wan(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        status = box.getEthernetLinkStatus()

        self.assertTrue(status)

    def test_ByteStatistic(self):
        box = Wan(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        statistic = box.getByteStatistic()

        self.assertTrue(statistic[0] >= 0)
        self.assertTrue(statistic[1] >= 0)

    def test_PacketStatistic(self):
        box = Wan(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        statistic = box.getPacketStatistic()

        self.assertTrue(statistic[0] >= 0)
        self.assertTrue(statistic[1] >= 0)

    def test_ConnectionInfo(self):
        box = Wan(hostname=defaults.test_host, port=defaults.test_port, protocol=defaults.test_protocol)
        box.setupTR64Device("fritz.box")
        box.username = defaults.test_user
        box.password = defaults.test_pw
        box.httpProxy = defaults.test_httpProxy
        box.httpsProxy = defaults.test_httpsProxy

        connectionInfo = box.getConnectionInfo()

        self.assertTrue(connectionInfo.enabled or not connectionInfo.enabled)
        self.assertTrue(connectionInfo.status)
        self.assertTrue(connectionInfo.type)
        self.assertTrue(connectionInfo.name)
        self.assertTrue(connectionInfo.uptime >= 0)
        self.assertTrue(connectionInfo.lastConnectionError)
        self.assertTrue(connectionInfo.connectionType)
        self.assertTrue(connectionInfo.natEnabled or not connectionInfo.natEnabled)
        self.assertTrue(connectionInfo.externalIPaddress)
        self.assertTrue(connectionInfo.dnsServers)
        self.assertTrue(connectionInfo.macAddress)
        self.assertTrue(connectionInfo.dnsEnabled or not connectionInfo.dnsEnabled)
        self.assertTrue(len(connectionInfo.raw.keys()) > 0)
