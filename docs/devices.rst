.. _devices:

Device Interaction
==================

Several devices which supports UPnP also support a way to control/run actions on the device. Certain devices, like TR64
supporting devices, let you totally configure and monitor any functionality. To be able to execute an actions the
following information's are needed:

    * Control URI
    * Namespace
    * Action name
    * Optional parameters

The control URI which is called to place the action and also the namespace aka service type is needed. The
namespace defines the scope or service type of the given action, the same action name can appear in different
namespaces.

Any device which supports TR64, DNLA or any other protocol which is based on UPnP can be controlled with this
library.

.. seealso::

    :meth:`~simpletr64.DeviceTR64.execute`

    The tools which have been provided with this library shows good use of the full library.

    `Additional short explanation of the UPnP protocol <http://www.upnp-hacks.org/upnp.html>`_

Protocol
--------

The protocol which controls/execute an action is based on the UPnP standard which itself uses SOAP. The following
python call:

.. code-block:: python

    >>> device = simpletr64.DeviceTR64(hostname=192.168.178.1, port=49000)
    ...
    >>> device.execute("/upnp/control/hosts", "urn:dslforum-org:service:Hosts:1", "GetGenericHostEntry", NewIndex=1)
    {'NewActive': '0', 'NewIPAddress': '192.168.0.23', 'NewMACAddress': '9C:20:7B:E7:FF:5F', 'NewInterfaceType':
        'Ethernet', 'NewHostName': 'Apple-TV', 'NewAddressSource': 'DHCP', 'NewLeaseTimeRemaining': '0'}

will create the following Action request:

  ::

    POST /upnp/control/hosts HTTP/1.1
    Host: 192.168.178.1:49000
    Content-Length: 422
    Accept-Encoding: gzip, deflate
    Soapaction: "urn:dslforum-org:service:Hosts:1#GetGenericHostEntry"
    Accept: */*
    User-Agent: python-requests/2.5.4.1 CPython/2.6.9 Darwin/15.2.0
    Connection: keep-alive
    Content-Type: text/xml; charset="UTF-8"

    <?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <soap:Header/>
        <soap:Body>
            <GetGenericHostEntry xmlns="urn:dslforum-org:service:Hosts:1">
                <NewIndex>1</NewIndex>
            </GetGenericHostEntry>
    </soap:Body>
    </soap:Envelope>

An example response:

  ::

    HTTP/1.1 200 OK
    DATE: Sat, 02 Jan 2016 14:12:44 GMT
    SERVER: FRITZ!Box Fon WLAN 7390 UPnP/1.0 AVM FRITZ!Box Fon WLAN 7390 84.06.30
    CONNECTION: keep-alive
    CONTENT-LENGTH: 576
    CONTENT-TYPE: text/xml; charset="utf-8"
    EXT:

    <?xml version="1.0"?>
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <s:Body>
    <u:GetGenericHostEntryResponse xmlns:u="urn:dslforum-org:service:Hosts:1">
    <NewIPAddress>192.168.0.23</NewIPAddress>
    <NewAddressSource>DHCP</NewAddressSource>
    <NewLeaseTimeRemaining>0</NewLeaseTimeRemaining>
    <NewMACAddress>9C:20:7B:E7:FF:5F</NewMACAddress>
    <NewInterfaceType>Ethernet</NewInterfaceType>
    <NewActive>0</NewActive>
    <NewHostName>Apple-TV</NewHostName>
    </u:GetGenericHostEntryResponse>
    </s:Body>
    </s:Envelope>

.. _authentication:

Authentication
--------------

Depending on the device and the settings some actions might need you to authenticate before you call the action. Again
depending on the device and the settings you might be requested to provide a username and password or some devices
might only ask for a password, please check your configuration. When you set username/password or just password the
authentication will be done transparently.

Example:

::

    device = DeviceTR64(...)
    device.password = "my secret"

.. seealso:: :meth:`~simpletr64.DeviceTR64.username`, :meth:`~simpletr64.DeviceTR64.password`

Proxies
-------

For any http/https call a proxy can be set, the way depends on the Class you use. The DeviceTR64 class supports it via
:meth:`~simpletr64.DeviceTR64.httpProxy` and :meth:`~simpletr64.DeviceTR64.httpsProxy`; the method
:meth:`~simpletr64.Discover.discoverParticularHost` in the
:class:`~simpletr64.Discover` class ask you to provide the proxy definition
for each call. Please, see the dedicated methods documentation for how to specify the proxies as the definition differs.

.. seealso::

    :meth:`~simpletr64.DeviceTR64.httpProxy`, :meth:`~simpletr64.DeviceTR64.httpsProxy`,
    :meth:`~simpletr64.Discover.discoverParticularHost`

Classes
-------

.. autoclass:: simpletr64.DeviceTR64
    :inherited-members:

