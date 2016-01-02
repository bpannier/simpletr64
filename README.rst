Simple TR64 UPnP: A simple way to talk to your UPnP and/or TR64 protocol devices
================================================================================

This library supports the discovery of UPnP devices in the local network and let you execute actions on them if
the device supports them. Also it contains a convenient way to execute TR64 protocol actions on route or other network
devices which supports TR64.

.. code-block:: python

    >>> results = simpletr64.discover()
    >>> results[0]
    LOC: http://192.168.178.1:49000/tr64desc.xml SRV: urn:dslforum-org:device:InternetGatewayDevice:1
    >>> device = simpletr64.DeviceTR64(hostname=192.168.178.1, port=49000)
    ...
    >>> device.execute("/upnp/control/hosts", "urn:dslforum-org:service:Hosts:1", "GetGenericHostEntry", NewIndex=1)
    {'NewActive': '0', 'NewIPAddress': '192.168.0.23', 'NewMACAddress': '9C:20:7B:E7:FF:5F', 'NewInterfaceType':
        'Ethernet', 'NewHostName': 'Apple-TV', 'NewAddressSource': 'DHCP', 'NewLeaseTimeRemaining': '0'}
    ...


Features
--------

- Discovery of UPnP devices in the local network
- Gathering of UPnP device information's
- Executing of UPnP actions
- Authentication for username/password or password only
- HTTP(S) proxy support
- Unicode

Installation
------------

To install Simple TR64, simply:

.. code-block:: bash

    $ pip install simpletr64
