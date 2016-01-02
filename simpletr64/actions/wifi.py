class Wifi:
    """Class to get Wifi information's of a device which supports ``urn:dslforum-org:service:WLANConfiguration:X``.

    The class supports devices which supports ``urn:dslforum-org:service:WLANConfiguration:X`` namespace. Unless the
    device is a AVM Fritz Box the DeviceTR64 objects needs to load the device definitions with
    :meth:`~simpletr64.DeviceTR64.loadDeviceDefinitions` before the usage of any of the methods. For a Fritz.box
    :meth:`~simpletr64.DeviceTR64.setupTR64Device` has to be called. Also a device might
    not support all of the actions. This class does not implement all of the actions of this namespace, please
    check the SCPD definitions if you miss some functionality. This library provides some tools to gather the
    needed information's.

    All Wifi actions ask for a device id, this depends on the device if the counting starts with 0 or 1. Often a device
    supports more than one device as for example to support 2.4 and 5 Ghz.

    .. seealso::

        :meth:`~simpletr64.DeviceTR64.loadDeviceDefinitions`, :meth:`~simpletr64.DeviceTR64.loadSCPD`,
        :meth:`~simpletr64.DeviceTR64.setupTR64Device`

        The tools which have been provided with this library shows good use of the full library.
    """
    def __init__(self, deviceTR64):
        """Initialize the object.

        :param DeviceTR64 deviceTR64: an initialized DeviceTR64 object
        :rtype: Wifi
        """
        self.__device = deviceTR64
        self.__namespace = "urn:dslforum-org:service:WLANConfiguration:"

    def getWifiInfo(self, wifiDeviceId):
        """Execute GetInfo action to get Wifi basic information's.

        :param wifiDeviceId: the id of the Wifi device
        :return: the basic informations
        :rtype: WifiBasicInfo
        """
        namespace = self.__namespace + str(wifiDeviceId)
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetInfo")

        return WifiBasicInfo(results)

    def getStatistic(self, wifiDeviceId):
        """Execute GetStatistics action to get Wifi statistics.

        :param wifiDeviceId: the id of the Wifi device
        :return: a tuple of two values, total packets sent and total packets received
        :rtype: list[int]
        """
        namespace = self.__namespace + str(wifiDeviceId)
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetStatistics")

        return [int(results["NewTotalPacketsSent"]), int(results["NewTotalPacketsReceived"])]

    def getPacketStatistic(self, wifiDeviceId):
        """Execute GetPacketStatistics action to get Wifi statistics.

        :param wifiDeviceId: the id of the Wifi device
        :return: a tuple of two values, total packets sent and total packets received
        :rtype: list[int]
        """
        namespace = self.__namespace + str(wifiDeviceId)
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetPacketStatistics")

        return [int(results["NewTotalPacketsSent"]), int(results["NewTotalPacketsReceived"])]

    def getTotalAssociations(self, wifiDeviceId):
        """Execute GetTotalAssociations action to get the amount of associated Wifi clients.

        :param wifiDeviceId: the id of the Wifi device
        :return: the amount of Wifi clients
        :rtype: int

        .. seealso:: :meth:`~simpletr64.actions.Wifi.getGenericAssociatedDeviceInfo`
        """
        namespace = self.__namespace + str(wifiDeviceId)
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetTotalAssociations")

        return int(results["NewTotalAssociations"])

    def getGenericAssociatedDeviceInfo(self, wifiDeviceId, index):
        """Execute GetGenericAssociatedDeviceInfo action to get detailed information about a Wifi client.

        :param wifiDeviceId: the id of the Wifi device
        :param index: the number of the client
        :return: the detailed information's about a Wifi client
        :rtype: WifiDeviceInfo

        .. seealso:: :meth:`~simpletr64.actions.Wifi.getTotalAssociations`
        """
        namespace = self.__namespace + str(wifiDeviceId)
        uri = self.__device.getControlURL(namespace)

        results = self.__device.execute(uri, namespace, "GetGenericAssociatedDeviceInfo",
                                        NewAssociatedDeviceIndex=index)

        return WifiDeviceInfo(results)


class WifiDeviceInfo:
    """A container class for Wifi device information's."""

    def __init__(self, results):
        """Initialize an object

        :param results: action results of an GetInfo action
        :type results: dict[str,str]
        :rtype: WifiDeviceInfo
        """
        self.__macAddress = results["NewAssociatedDeviceMACAddress"]
        self.__ipAddress = results["NewAssociatedDeviceIPAddress"]
        self.__authenticated = bool(results["NewAssociatedDeviceAuthState"])
        self.__raw = results

    @property
    def raw(self):
        """Return the raw results which have been used to initialize the object.

        :return: the raw results
        :rtype: dict[str,str]
        """
        return self.__raw

    @property
    def macAddress(self):
        """Returns the mac address

        :return: the mac address
        :rtype: str
        """
        return self.__macAddress

    @property
    def ipAddress(self):
        """Return the IP address

        :return: the IP address
        :rtype: str
        """
        return self.__ipAddress

    @property
    def authenticated(self):
        """Returns if the client has been authenticated.

        :return: if client is authenticated
        :rtype: bool
        """
        return self.__authenticated


class WifiBasicInfo:
    """A container class for Wifi client information's."""
    def __init__(self, results):
        """Initialize an object

        :param results: action results of an GetInfo action
        :type results: dict[str,str]
        :rtype: WifiBasicInfo
        """
        self.__enabled = bool(results["NewEnable"])
        self.__status = results["NewStatus"]
        self.__channel = int(results["NewChannel"])
        self.__ssid = results["NewSSID"]
        self.__beaconType = results["NewBeaconType"]
        self.__macControl = bool(results["NewMACAddressControlEnabled"])
        self.__standard = results["NewStandard"]
        self.__bssid = results["NewBSSID"]
        self.__encryptionMode = results["NewBasicEncryptionModes"]
        self.__authMode = results["NewBasicAuthenticationMode"]
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
        """Returns if the Wifi client is enabled.

        :return: if client is enabled.
        :rtype: bool
        """
        return self.__enabled

    @property
    def status(self):
        """Returns the status for the Wifi client.

        :return: the status for the client
        :rtype: str
        """
        return self.__status

    @property
    def channel(self):
        """Returns the used Wifi channel.

        :return: the used Wifi channel
        :rtype: int
        """
        return self.__channel

    @property
    def ssid(self):
        """Return the SSID for the given Wifi client.

        :return: the SSID
        :rtype: str
        """
        return self.__ssid

    @property
    def beaconType(self):
        """Return ... what ever

        :return:
        :rtype: str
        """
        return self.__beaconType

    @property
    def macControl(self):
        """Returns if mac control is activated.

        :return: if mac control is activated
        :rtype: bool
        """
        return self.__macControl

    @property
    def standard(self):
        """Return ... what ever

        :return:
        :rtype: str
        """
        return self.__standard

    @property
    def bssid(self):
        """Returns the BSS id.

        :return: the bss id.
        :rtype: str
        """
        return self.__bssid

    @property
    def encryptionMode(self):
        """Returns the encryption mode.

        :return: the encryption mode
        :rtype: str
        """
        return self.__encryptionMode

    @property
    def authMode(self):
        """Return the authentication mode for the Wifi client.

        :return: the authentication mode for the Wifi client
        :rtype: str
        """
        return self.__authMode
