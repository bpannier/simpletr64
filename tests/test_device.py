import unittest

from simpletr64.devicetr64 import DeviceTR64


class TestBox(unittest.TestCase):

    def test_Defaul(self):
        box = DeviceTR64("box")
        self.assertEqual(box.host, "box")
        self.assertEqual(box.port, 49000)
        self.assertEqual(box.protocol, "http")

    def test_Port(self):
        box = DeviceTR64("box", port=1234)
        self.assertEqual(box.host, "box")
        self.assertEqual(box.port, 1234)
        self.assertEqual(box.protocol, "http")

    def test_Encryption(self):
        box = DeviceTR64("some", protocol="https")
        self.assertEqual(box.host, "some")
        self.assertEqual(box.port, 49000)
        self.assertEqual(box.protocol, "https")

    def test_username(self):
        box = DeviceTR64("some")
        self.assertEqual(box.username, "")
        box.username = "abc"
        self.assertEqual(box.username, "abc")

    def test_pw(self):
        box = DeviceTR64("some")
        self.assertEqual(box.password, "")
        box.password = "abc123"
        self.assertEqual(box.password, "abc123")

    def test_deviceSetup(self):
        box = DeviceTR64("some")
        self.assertEqual(len(box.deviceServiceDefinitions), 0)
        box.setupTR64Device("fritz.box")
        self.assertTrue(len(box.deviceServiceDefinitions) > 0)

