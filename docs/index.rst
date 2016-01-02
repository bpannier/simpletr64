.. Simple TR64 UPnP documentation master file, created by
   sphinx-quickstart on Sun Dec 27 17:22:46 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Simple TR64 UPnP
================

Release v\ |version|. (:ref:`Installation <install>`)

This library supports the discovery of UPnP devices in the local network and let you execute actions on them if
the device supports them. Also it contains a convenient way to execute TR64 protocol actions on route or other network
devices which supports TR64.

Discover and execute:

.. code-block:: python

    >>> results = simpletr64.discover()
    >>> print(results[0])
    LOC: http://192.168.178.1:49000/tr64desc.xml SRV: urn:dslforum-org:device:InternetGatewayDevice:1
    ...
    >>> device = simpletr64.DeviceTR64(hostname=192.168.178.1, port=49000)
    ...
    >>> device.execute("/upnp/control/hosts", "urn:dslforum-org:service:Hosts:1", "GetGenericHostEntry", NewIndex=1)
    {'NewActive': '0', 'NewIPAddress': '192.168.0.23', 'NewMACAddress': '9C:20:7B:E7:FF:5F', 'NewInterfaceType':
        'Ethernet', 'NewHostName': 'Apple-TV', 'NewAddressSource': 'DHCP', 'NewLeaseTimeRemaining': '0'}

or even easier, execute:

.. code-block:: python

    >>> device = DeviceTR64("fritz.box")
    >>> device.setupTR64Device("fritz.box")
    >>> system = System(device)
    >>> print(system.getSystemInfo().manufactureName)
    "AVM"

Documentation
-------------
.. toctree::
    :maxdepth: 2

    install
    discover
    devices
    tr64

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

