
import unittest

from simpletr64.devicetr64 import DeviceTR64

class TestLan(unittest.TestCase):

    def test_AmountOfHostsConnected(self):
        data = """<?xml version="10"?>
<root
  xmlns="urn:schemas-upnp-org:device-1-0"
  xmlns:ms="urn:microsoft-com:wmc-1-0"
  xmlns:pnpx="http://schemasmicrosoftcom/windows/pnpx/2005/11"
  xmlns:df="http://schemasmicrosoftcom/windows/2008/09/devicefoundation"
  xmlns:yamaha="urn:schemas-yamaha-com:device-1-0">
    <yamaha:X_device><yamaha:X_URLBase>http://REDACTED:80/</yamaha:X_URLBase><yamaha:X_serviceList><yamaha:X_service><yamaha:X_specType>urn:schemas-yamaha-com:service:X_YamahaRemoteControl:1</yamaha:X_specType><yamaha:X_controlURL>/YamahaRemoteControl/ctrl</yamaha:X_controlURL><yamaha:X_unitDescURL>/YamahaRemoteControl/descxml</yamaha:X_unitDescURL></yamaha:X_service></yamaha:X_serviceList></yamaha:X_device>
    <specVersion>
        <major>1</major>
        <minor>0</minor>
    </specVersion>
    <device
      ms:X_MS_SupportsWMDRM="true">
        <dlna:X_DLNADOC xmlns:dlna="urn:schemas-dlna-org:device-1-0">DMR-150</dlna:X_DLNADOC>
        <pnpx:X_compatibleId>MS_DigitalMediaDeviceClass_DMR_V001
                </pnpx:X_compatibleId>
        <pnpx:X_deviceCategory>MediaDevices MultimediaDMR MediaDeviceDMC
                </pnpx:X_deviceCategory>
        <pnpx:X_hardwareId>VEN_0033&amp;DEV_0006&amp;REV_01
                </pnpx:X_hardwareId>
        <df:X_deviceCategory>MultimediaDMR
                </df:X_deviceCategory>
        <deviceType>urn:schemas-upnp-org:device:MediaRenderer:1</deviceType>
        <friendlyName>Pascal</friendlyName>
        <manufacturer>Yamaha Corporation</manufacturer>
        <manufacturerURL>http://wwwyamahacom/</manufacturerURL>
        <modelDescription>AV Receiver</modelDescription>
        <modelName>RX-V475</modelName>
        <modelNumber>V475</modelNumber>
        <modelURL>http://wwwyamahacom/</modelURL>
        <serialNumber>REDACTED</serialNumber>
        <UDN>REDACTED</UDN>
        <UPC>REDACTED</UPC>
        <iconList>
            <icon>
                <mimetype>image/jpeg</mimetype>
                <width>48</width>
                <height>48</height>
                <depth>24</depth>
                <url>/BCO_device_sm_iconjpg</url>
            </icon>
            <icon>
                <mimetype>image/jpeg</mimetype>
                <width>120</width>
                <height>120</height>
                <depth>24</depth>
                <url>/BCO_device_lrg_iconjpg</url>
            </icon>
            <icon>
                <mimetype>image/png</mimetype>
                <width>48</width>
                <height>48</height>
                <depth>24</depth>
                <url>/BCO_device_sm_iconpng</url>
            </icon>
            <icon>
                <mimetype>image/png</mimetype>
                <width>120</width>
                <height>120</height>
                <depth>24</depth>
                <url>/BCO_device_lrg_iconpng</url>
            </icon>
        </iconList>
        <serviceList>
            <service>
                <serviceType>urn:schemas-upnp-org:service:RenderingControl:1</serviceType>
                <serviceId>urn:upnp-org:serviceId:RenderingControl</serviceId>
                <SCPDURL>/RenderingControl/descxml</SCPDURL>
                <controlURL>/RenderingControl/ctrl</controlURL>
                <eventSubURL>/RenderingControl/evt</eventSubURL>
            </service>
            <service>
                <serviceType>urn:schemas-upnp-org:service:ConnectionManager:1</serviceType>
                <serviceId>urn:upnp-org:serviceId:ConnectionManager</serviceId>
                <SCPDURL>/ConnectionManager/descxml</SCPDURL>
                <controlURL>/ConnectionManager/ctrl</controlURL>
                <eventSubURL>/ConnectionManager/evt</eventSubURL>
            </service>
            <service>
                <serviceType>urn:schemas-upnp-org:service:AVTransport:1</serviceType>
                <serviceId>urn:upnp-org:serviceId:AVTransport</serviceId>
                <SCPDURL>/AVTransport/descxml</SCPDURL>
                <controlURL>/AVTransport/ctrl</controlURL>
                <eventSubURL>/AVTransport/evt</eventSubURL>
            </service>
        </serviceList>
        <presentationURL>http://REDACTED/</presentationURL>
    </device>
</root>"""

        url = "http://pascalfritzbox:8080/MediaRenderer/desc.xml"
        box = DeviceTR64.createFromURL(url)

        box._loadDeviceDefinitions(url, data)

        self.assertTrue(len(box.deviceServiceDefinitions.keys()) > 0)