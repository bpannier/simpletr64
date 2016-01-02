.. _devices:

Device Interaction
==================

.. seealso::

    The tools which have been provided with this library shows good use of the full library.

    `Additional short explanation of the UPnP protocol <http://www.upnp-hacks.org/upnp.html>`_

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

