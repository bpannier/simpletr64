.. :changelog:

Release History
---------------

1.0.3 (2016-xx-xx)
++++++++++++++++++
* Added timeout to any TR64 action
* Fix reboot action

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

