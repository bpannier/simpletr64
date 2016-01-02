class Wan:
    """Class to get various WAN information's of a device which supports ``urn:dslforum-org:service:WAN*``.

    The class supports devices which supports ``urn:dslforum-org:service:WAN* namespace``. Unless the
    device is a AVM Fritz Box the DeviceTR64 objects needs to load the device definitions with
    :meth:`~simpletr64.DeviceTR64.loadDeviceDefinitions` before the usage of any of the methods. For a Fritz.box
    :meth:`~simpletr64.DeviceTR64.setupTR64Device` has to be called. Also a device might
    not support all of the actions. This class does not implement all of the actions of this namespace, please
    check the SCPD definitions if you miss some functionality. This library provides some tools to gather the
    needed information's.

    .. seealso::

        :meth:`~simpletr64.DeviceTR64.loadDeviceDefinitions`, :meth:`~simpletr64.DeviceTR64.loadSCPD`,
        :meth:`~simpletr64.DeviceTR64.setupTR64Device`

        The tools which have been provided with this library shows good use of the full library.
    """

    def __init__(self, deviceTR64):
        """Initialize the object.

        :param DeviceTR64 deviceTR64: an initialized DeviceTR64 object
        :rtype: Wan
        """
        self.__device = deviceTR64

    def getLinkInfo(self):
        """Execute GetInfo action to get basic WAN link information's.

        :return: basic WAN link information's
        :rtype: WanLinkInfo
        """
        namespace = "urn:dslforum-org:service:WANDSLInterfaceConfig:1"
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetInfo")

        return WanLinkInfo(results)

    def getLinkProperties(self):
        """Execute GetCommonLinkProperties action to get WAN link properties.

        :return: WAN link properties
        :rtype: WanLinkProperties
        """
        namespace = "urn:dslforum-org:service:WANCommonInterfaceConfig:1"
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetCommonLinkProperties")

        return WanLinkProperties(results)

    def getADSLInfo(self):
        """Execute GetInfo action to get basic ADSL information's.

        :return: ADSL informations.
        :rtype: ADSLInfo
        """
        namespace = "urn:dslforum-org:service:WANDSLLinkConfig:1"
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetInfo")

        return ADSLInfo(results)

    def getEthernetLinkStatus(self):
        """Execute GetEthernetLinkStatus action to get the status of the ethernet link.

        :return: status of the ethernet link
        :rtype: str
        """
        namespace = "urn:dslforum-org:service:WANEthernetLinkConfig:1"
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetEthernetLinkStatus")

        return results["NewEthernetLinkStatus"]

    def getByteStatistic(self):
        """Execute GetTotalBytesSent&GetTotalBytesReceived actions to get WAN statistics.

        :return: a tuple of two values, total bytes sent and total bytes received
        :rtype: list[int]
        """
        namespace = "urn:dslforum-org:service:WANCommonInterfaceConfig:1"
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetTotalBytesSent")
        results2 = self.__device.execute(uri, namespace, "GetTotalBytesReceived")

        return [int(results["NewTotalBytesSent"]),
                int(results2["NewTotalBytesReceived"])]

    def getPacketStatistic(self):
        """Execute GetTotalPacketsSent&GetTotalPacketsReceived actions to get WAN statistics.

        :return: a tuple of two values, total packets sent and total packets received
        :rtype: list[int]
        """
        namespace = "urn:dslforum-org:service:WANCommonInterfaceConfig:1"
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetTotalPacketsSent")
        results2 = self.__device.execute(uri, namespace, "GetTotalPacketsReceived")

        return [int(results["NewTotalPacketsSent"]),
                int(results2["NewTotalPacketsReceived"])]

    def getConnectionInfo(self):
        """Execute GetInfo action to get WAN connection information's.

        :return: WAN connection information's.
        :rtype: ConnectionInfo
        """
        namespace = "urn:dslforum-org:service:WANIPConnection:1"
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetInfo")

        return ConnectionInfo(results)


class WanLinkInfo:
    """A container class for WAN link information's."""

    def __init__(self, results):
        """Initialize an object

        :param results: action results of an GetInfo action
        :type results: dict[str,str]
        :rtype: WanLinkInfo
        """
        self.__enabled = bool(results["NewEnable"])
        self.__status = results["NewStatus"]
        self.__dataPath = results["NewDataPath"]
        self.__upstreamCurrentRate = int(results["NewUpstreamCurrRate"])
        self.__downstreamCurrentRate = int(results["NewDownstreamCurrRate"])
        self.__upstreamMaxRate = int(results["NewUpstreamMaxRate"])
        self.__downstreamMaxRate = int(results["NewDownstreamMaxRate"])
        self.__raw = results

    @property
    def raw(self):
        """Return the raw results which have been used to initialize the object.

        :return: the raw results
        :rtype: dict[str,str]
        """
        return self.__raw

    @property
    def enabled(self):
        """Return if the WAN link is enabled.

        :return: if the WAN link is enabled.
        :rtype: bool
        """
        return self.__enabled

    @property
    def status(self):
        """Return the WAN link status.

        :return: the WAN link status.
        :rtype: str
        """
        return self.__status

    @property
    def dataPath(self):
        """Return .... what

        :return:
        :rtype: str
        """
        return self.__dataPath

    @property
    def upstreamCurrentRate(self):
        """Return the current upstream rate of the WAN link.

        :return: the current upstream rate of the WAN link.
        :rtype: int
        """
        return self.__upstreamCurrentRate

    @property
    def downStreamCurrentRate(self):
        """Return the current downstream rate of the WAN link.

        :return: the current downstream rate of the WAN link.
        :rtype: int
        """
        return self.__downstreamCurrentRate

    @property
    def upstreamMaxRate(self):
        """Return the maximal upstream rate of the WAN link.

        :return: the maximal upstream rate of the WAN link.
        :rtype: int
        """
        return self.__upstreamMaxRate

    @property
    def downstreamMaxRate(self):
        """Return the maximal downstream rate of the WAN link.

        :return: the maximal downstream rate of the WAN link.
        :rtype: int
        """
        return self.__downstreamMaxRate


class ADSLInfo:
    """A container class for ADSL link information's."""

    def __init__(self, results):
        """Initialize an object

        :param results: action results of an GetInfo action
        :type results: dict[str,str]
        :rtype: ADSLInfo
        """
        self.__enabled = bool(results["NewEnable"])
        self.__status = results["NewLinkStatus"]
        self.__linkType = results["NewLinkType"]
        self.__destinationAddress = results["NewDestinationAddress"]
        self.__raw = results

    @property
    def raw(self):
        """Return the raw results which have been used to initialize the object.

        :return: the raw results
        :rtype: dict[str,str]
        """
        return self.__raw

    @property
    def enabled(self):
        """Return if the ADSL interface is enabled.

        :return: if the ADSL interface is enabled.
        :rtype: bool
        """
        return self.__enabled

    @property
    def status(self):
        """Return the status for the ADSL interface.

        :return: the status for the ADSL interface.
        :rtype: str
        """
        return self.__status

    @property
    def linkType(self):
        """Return the link type for the ADSL interface.

        :return: Return the link type for the ADSL interface.
        :rtype: str
        """
        return self.__linkType

    @property
    def destinationAddress(self):
        """Return the destination address of the ADSL interface.

        :return: the destination address of the ADSL interface.
        :rtype: str
        """

        return self.__destinationAddress


class WanLinkProperties:
    """A container class for WAN link properties."""

    def __init__(self, results):
        """Initialize an object

        :param results: action results of an GetCommonLinkProperties action
        :type results: dict[str,str]
        :rtype: WanLinkProperties
        """
        self.__accessType = results["NewWANAccessType"]
        self.__upstreamMaxBitRate = int(results["NewLayer1UpstreamMaxBitRate"])
        self.__downstreamMaxBitRate = int(results["NewLayer1DownstreamMaxBitRate"])
        self.__linkStatus = results["NewPhysicalLinkStatus"]
        self.__raw = results

    @property
    def raw(self):
        """Return the raw results which have been used to initialize the object.

        :return: the raw results
        :rtype: dict[str,str]
        """
        return self.__raw

    @property
    def accessType(self):
        """Return the access type of the WAN link.

        :return: the access type of the WAN link.
        :rtype: str
        """
        return self.__accessType

    @property
    def linkStatus(self):
        """Return the WAN link status.

        :return: the WAN link status.
        :rtype: str
        """
        return self.__linkStatus

    @property
    def upstreamMaxBitRate(self):
        """Return the maximum bit rate for the upstream on this WAN link.

        :return: the maximum bit rate for the upstream on this WAN link.
        :rtype: int
        """
        return self.__upstreamMaxBitRate

    @property
    def downstreamMaxBitRate(self):
        """Return the maximum bit rate for the downstream on this WAN link.

        :return: the maximum bit rate for the downstream on this WAN link.
        :rtype: int
        """
        return self.__downstreamMaxBitRate


class ConnectionInfo:
    """A container class for WAN connection information's."""

    def __init__(self, results):
        """Initialize an object

        :param results: action results of an GetInfo action
        :type results: dict[str,str]
        :rtype: ConnectionInfo
        """
        self.__enabled = bool(results["NewEnable"])
        self.__status = results["NewConnectionStatus"]
        self.__type = results["NewConnectionType"]
        self.__name = results["NewName"]
        self.__uptime = int(results["NewUptime"])
        self.__connectionType = results["NewConnectionType"]
        self.__lastConnectionError = results["NewLastConnectionError"]
        self.__natEnabled = bool(results["NewNATEnabled"])
        self.__externalIPaddress = results["NewExternalIPAddress"]
        self.__dnsServers = results["NewDNSServers"]
        self.__macAddress = results["NewMACAddress"]
        self.__dnsEnabled = bool(results["NewDNSEnabled"])
        self.__raw = results

    @property
    def raw(self):
        """Return the raw results which have been used to initialize the object.

        :return: the raw results
        :rtype: dict[str,str]
        """
        return self.__raw

    @property
    def enabled(self):
        """Return if WAN connection is enabled.

        :return: if WAN connection is enabled.
        :rtype: bool
        """
        return self.__enabled

    @property
    def status(self):
        """Return the status of the WAN connection.

        :return: the status of the WAN connection.
        :rtype: str
        """
        return self.__status

    @property
    def type(self):
        """Return the type of the WAN connection.

        :return: the type of the WAN connection.
        :rtype: str
        """
        return self.__type

    @property
    def name(self):
        """Return the name of the WAN connection.

        :return: the name of the WAN connection.
        :rtype: str
        """
        return self.__name

    @property
    def uptime(self):
        """Return the uptime of the WAN connection.

        :return: the uptime of the WAN connection.
        :rtype: int
        """
        return self.__uptime

    @property
    def lastConnectionError(self):
        """Return the last connection error of the WAN connection.

        :return: the last connection error of the WAN connection.
        :rtype: str
        """
        return self.__lastConnectionError

    @property
    def connectionType(self):
        """Return the type of the WAN connection.

        :return: the type of the WAN connection.
        :rtype: str
        """
        return self.__connectionType

    @property
    def natEnabled(self):
        """Return if NAT is enabled for the WAN connection.

        :return: if NAT is enabled for the WAN connection.
        :rtype: bool
        """
        return self.__natEnabled

    @property
    def externalIPaddress(self):
        """Return the external IP address of the WAN connection.

        :return: the external IP address of the WAN connection.
        :rtype: str
        """
        return self.__externalIPaddress

    @property
    def dnsServers(self):
        """Return the list of DNS servers for the WAN connection.

        :return: the list of DNS servers for the WAN connection.
        :rtype: str
        """
        return self.__dnsServers

    @property
    def macAddress(self):
        """Return the MAC address of the WAN device.

        :return: the MAC address of the WAN device.
        :rtype: str
        """
        return self.__macAddress

    @property
    def dnsEnabled(self):
        """Return if DNS is enabled for the WAN connection.

        :return: if DNS is enabled for the WAN connection.
        :rtype: bool
        """
        return self.__dnsEnabled
