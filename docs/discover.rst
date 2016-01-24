.. _discover:

Discover UPnP Devices
=====================

The UPnP protocol is used to discover certain devices in the local network and to a certain extend also to interact
with them.

The discovery mechanism is to send a multicast request which gets answered by UPnP devices in the
HTTP format. The combination of devices in potential stand-by mode and multicast let the discovery fail infrequently.
For that reason a retry is strongly recommended to make sure to get answers from all UPnP device in the
network. Also the service type which is included in the request matters for some devices, it is recommended to use the
most specific service type, if known, for a device as some devices answers differently depending on the service type.
Recommendation is to use after a broader :meth:`~simpletr64.Discover.discover` the more specific
:meth:`~simpletr64.Discover.discoverParticularHost` again for every device you are interested in as that method
do some magic to find all the information's which a device can provide.

The discovery mechanism is the only way to gather the URL to the device specifications, which is needed if you like
to interact with a device. Not all UPnP devices support an interaction based on the standard and provide only a
proprietary way for which you need the vendor documentation.

This library provides an sheell command 'upnp_tools' which shows how to use the library for the different use
cases.

.. seealso::

    The scripts which have been provided with this library shows good use of the full library.

    `Additional short explanation of the UPnP protocol <http://www.upnp-hacks.org/upnp.html>`_

Protocol
--------

This example illustrates what the library sends and receives during a discovery process, whereas the example is given
for a specific service type.

Request:

A discovery request is send via IP multicast on 239.255.255.250:1900.

  ::

    M-SEARCH * HTTP/1.1\r\n
    MX: 5\r\n
    MAN: "ssdp:discover"\r\n
    HOST: 239.255.255.250:1900\r\n
    ST: urn:dslforum-org:device:InternetGatewayDevice:1\r\n
    \r\n

Response:
  ::

    HTTP/1.1 200 OK\r\n
    LOCATION: http://192.168.178.1:49000/tr64desc.xml\r\n
    SERVER: FRITZ!Box Fon WLAN 7390 UPnP/1.0 AVM FRITZ!Box Fon WLAN 7390 84.06.30\r\n
    CACHE-CONTROL: max-age=1800\r\n
    EXT:\r\n
    ST: urn:dslforum-org:device:InternetGatewayDevice:1\r\n
    USN: uuid:739f2419-bccb-40e7-8e6c-BC254222D5C4::urn:dslforum-org:device:InternetGatewayDevice:1\r\n
    \r\n


Classes
-------

.. autoclass:: simpletr64.Discover
    :inherited-members:

****

.. autoclass:: simpletr64.DiscoveryResponse
    :members:
