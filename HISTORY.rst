.. :changelog:

Release History
---------------

1.0.6 (2016-01-xx)
++++++++++++++++++

* Fix error in upnp_tools when no command was given

1.0.5 (2016-01-15)
++++++++++++++++++

* Adding the support for DNLA devices which announce some device definitions slightly differently
* Moving all tools/ scripts into one "upnp_tools" script and move it to bin so it get installed into exe path

1.0.4 (2016-01-11)
++++++++++++++++++

* Adding Fritz specific actions
* Fix a bug with installing the package, thanks to Raphael Sobik

1.0.3 (2016-01-08)
++++++++++++++++++

* Added timeout to any TR64 action
* Added getSpecificAssociatedDeviceInfo in Wifi actions
* Added setEnable to toggle the LAN/WAN/Wifi interface on/off
* Added setSSID and setChannel to set these Wifi interface parameters accordingly
* Added softwareUpdateAvailable
* Added requestConnection and terminateConnection for a WAN connection
* Added AVM Fritz Box product specific capabilities in new Fritz class
* Fix reboot action
* Fix all TR64 actions with bool results which were always True

1.0.2 (2016-01-06)
++++++++++++++++++

* Added the ability to request the namespace for a TR64 action
* Added interface ID's to all actions in Lan, Wan and Wifi
* Added a factory method to DeviceTR64 which takes an URL to the device definitions
* Improved error handling on XML parsing problems of any content
* Changed the declaration of getGenericAssociatedDeviceInfo for consistency reasons
* Changed for all Wifi actions that the interface id is now optional
* Changed all TR64 action classes to be a sub class of DeviceTR64
* Fix an issue with relative URL's in the device definition

1.0.1 (2016-01-04)
++++++++++++++++++

* Added better error reporting
* Added timeout to any network interaction
* added the possibility to discover more than one service at the same time
* fixed getHostDetailsByMACAddress()

1.0.0 (2016-01-02)
++++++++++++++++++

* Birth!

