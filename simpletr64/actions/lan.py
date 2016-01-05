class Lan:
    """Class to get various LAN information's of a device which supports ``urn:dslforum-org:service:Hosts:1`` and
    ``urn:dslforum-org:service:LAN*``.

    The class supports devices which supports ``urn:dslforum-org:service:LAN*`` and ``urn:dslforum-org:service:Hosts:1``
    namespace. Unless the device is a AVM Fritz Box the DeviceTR64 objects needs to load the device definitions with
    :meth:`~simpletr64.DeviceTR64.loadDeviceDefinitions` before the usage of any of the methods.
    For a Fritz.box :meth:`~simpletr64.DeviceTR64.setupTR64Device` has to be called. Also a device might
    not support all of the actions. This class does not implement all of the actions of this namespace, please
    check the SCPD definitions if you miss some functionality. This library provides some tools to gather the
    needed information's.

    .. seealso::

        :meth:`~simpletr64.DeviceTR64.loadDeviceDefinitions`, :meth:`~simpletr64.DeviceTR64.loadSCPD`,
        :meth:`~simpletr64.DeviceTR64.setupTR64Device`

        The tools which have been provided with this library shows good use of the full library.
    """

    serviceTypeLookup = {
        "getAmountOfHostsConnected": "urn:dslforum-org:service:Hosts:1",
        "getHostDetailsByIndex": "urn:dslforum-org:service:Hosts:1",
        "getHostDetailsByMACAddress": "urn:dslforum-org:service:Hosts:1",
        "getEthernetInfo": "urn:dslforum-org:service:LANEthernetInterfaceConfig:1",
        "getEthernetStatistic": "urn:dslforum-org:service:LANEthernetInterfaceConfig:1"
    }

    def __init__(self, deviceTR64):
        """Initialize the object.

        :param DeviceTR64 deviceTR64: an initialized DeviceTR64 object
        :rtype: Lan
        """
        self.__device = deviceTR64

    @staticmethod
    def getServiceType(method):
        """For a given method name return the service type which supports it.

        :param method: the method name to lookup
        :return: the service type or None
        :rtype: str
        """
        if method in Lan.serviceTypeLookup.keys():
            return Lan.serviceTypeLookup[method]
        return None

    def getAmountOfHostsConnected(self):
        """Execute NewHostNumberOfEntries action to get the amount of known hosts.

        :return: the amount of known hosts.
        :rtype: int

        .. seealso:: :meth:`~simpletr64.actions.Lan.getHostDetailsByIndex`
        """
        namespace = Lan.getServiceType("getAmountOfHostsConnected")
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetHostNumberOfEntries")

        return int(results["NewHostNumberOfEntries"])

    def getHostDetailsByIndex(self, index):
        """Execute GetGenericHostEntry action to get detailed information's of a connected host.

        :param index: the index of the host
        :return: the detailed information's of a connected host.
        :rtype: HostDetails

        .. seealso:: :meth:`~simpletr64.actions.Lan.getAmountOfHostsConnected`
        """
        namespace = Lan.getServiceType("getHostDetailsByIndex")
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetGenericHostEntry", NewIndex=index)

        return HostDetails(results)

    def getHostDetailsByMACAddress(self, macAddress):
        """Get host details for a host specified by its MAC address.

        :param str macAddress: MAC address in the form ``38:C9:86:26:7E:38``
        :return: return the host details if found otherwise an Exception will be raised
        :rtype: HostDetails
        """
        namespace = Lan.getServiceType("getHostDetailsByMACAddress")
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetSpecificHostEntry", NewMACAddress=macAddress)

        return HostDetails(results, macAddress=macAddress)

    def getEthernetInfo(self):
        """Execute GetInfo action to get information's about the Ethernet interface.

        :return: information's about the Ethernet interface.
        :rtype: EthernetInfo
        """
        namespace = Lan.getServiceType("getEthernetInfo")
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetInfo")

        return EthernetInfo(results)

    def getEthernetStatistic(self):
        """Execute GetStatistics action to get statistics of the Ethernet interface.

        :return: statisticss of the Ethernet interface.
        :rtype: EthernetStatistic
        """
        namespace = Lan.getServiceType("getEthernetStatistic")
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetStatistics")

        return EthernetStatistic(results)


class EthernetStatistic:
    """A container class for Ethernet interface statistics."""

    def __init__(self, results):
        """Initialize an object

        :param results: action results of an GetStatistics action
        :type results: dict[str,str]
        :rtype: EthernetStatistic
        """
        self.__bytesSent = int(results["NewBytesSent"])
        self.__bytesReceived = int(results["NewBytesReceived"])
        self.__packetsSent = int(results["NewPacketsSent"])
        self.__packetsReceived = int(results["NewPacketsReceived"])
        self.__raw = results

    @property
    def raw(self):
        """Return the raw results which have been used to initialize the object.

        :return: the raw results
        :rtype: dict[str,str]
        """
        return self.__raw

    @property
    def bytesSent(self):
        """Return the amount of bytes which have been sent.

        :return: the amount of bytes which have been sent.
        :rtype: int
        """
        return self.__bytesSent

    @property
    def bytesReceived(self):
        """Return the amount of bytes which have been received.

        :return: the amount of bytes which have been received.
        :rtype: int
        """
        return self.__bytesReceived

    @property
    def packetsSent(self):
        """Return the amount of packets which have been sent.

        :return: the amount of packets which have been sent.
        :rtype: int
        """
        return self.__packetsSent

    @property
    def packetsReceived(self):
        """Return the amount of packets which have been received.

        :return: the amount of packets which have been received.
        :rtype: int
        """
        return self.__packetsReceived


class EthernetInfo:
    """A container class for Ethernet interface information's."""

    def __init__(self, results):
        """Initialize an object

        :param results: action results of an GetInfo action
        :type results: dict[str,str]
        :rtype: EthernetInfo
        """
        self.__enabled = bool(results["NewEnable"])
        self.__status = results["NewStatus"]
        self.__macAddress = results["NewMACAddress"]
        self.__maxBitRate = results["NewMaxBitRate"]
        self.__duplexMode = results["NewDuplexMode"]
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
        """Return if the interface is enabled.

        :return: if the interface is enabled.
        :rtype: bool
        """
        return self.__enabled

    @property
    def status(self):
        """Return the status of the interface.

        :return: the status of the interface.
        :rtype: str
        """
        return self.__status

    @property
    def macAddress(self):
        """Return the MAC address of the ethernet interface.

        :return: the MAC address of the ethernet interface.
        :rtype: str
        """
        return self.__macAddress

    @property
    def maxBitRate(self):
        """Return the max bit rate of the interface.

        :return: the max bit rate of the interface.
        :rtype: str
        """
        return self.__maxBitRate

    @property
    def duplexMode(self):
        """Return if the Ethernet interface is in half or full duplex mode.

        :return: if the Ethernet interface is in half or full duplex mode.
        :rtype: str
        """
        return self.__duplexMode


class HostDetails:
    """A container class for information's about a LAN connected host."""

    def __init__(self, results, macAddress=None):
        """Initialize an object

        :param results: action results of an GetSpecificHostEntry or GetGenericHostEntry action
        :param str macAddress: in the result for GetSpecificHostEntry is no Mac Address, lets add it again
        :type results: dict[str,str]
        :rtype: HostDetails
        """
        if "NewMACAddress" in results.keys():
            self.__macAddress = results["NewMACAddress"]
        else:
            self.__macAddress = macAddress

        self.__ipAddress = results["NewIPAddress"]
        self.__hostname = results["NewHostName"]
        self.__interface = results["NewInterfaceType"]
        self.__source = results["NewAddressSource"]
        self.__leaseTime = int(results["NewLeaseTimeRemaining"])
        self.__active = bool(results["NewActive"])
        self.__raw = results

    @property
    def raw(self):
        """Return the raw results which have been used to initialize the object.

        :return: the raw results
        :rtype: dict[str,str]
        """
        return self.__raw

    @property
    def ipaddress(self):
        """Return the IP address of the host.

        :return: the IP address of the host.
        :rtype: str
        """
        return self.__ipAddress

    @property
    def hostname(self):
        """Return the name of the host.

        :return: the name of the host.
        :rtype: str
        """
        return self.__hostname

    @property
    def macAddress(self):
        """Return the MAC address of the host.

        :return: the MAC address of the host.
        :rtype: str
        """
        return self.__macAddress

    @property
    def interface(self):
        """Return the interface to which the host is connected.

        :return: the interface to which the host is connected.
        :rtype: str
        """
        return self.__interface

    @property
    def source(self):
        """Return the source where the address of this host was learned.

        :return: the source where the address of this host was learned.
        :rtype str:
        """
        return self.__source

    @property
    def leasetime(self):
        """Return the remaining lease time

        :return: the remaining lease time
        :rtype: int
        """
        return self.__leaseTime

    @property
    def active(self):
        """Return if the host is active.

        :return: if the host is active
        :rtype: bool
        """
        return self.__active
