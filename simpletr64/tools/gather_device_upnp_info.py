# For a given device finds/load all TR64 informations and print them to stdout
# Device must be reachable via multicast.


import argparse
import copy
import json
from simpletr64.devicetr64 import DeviceTR64
from simpletr64.discover import Discover

#######################################################################################################################

parser = argparse.ArgumentParser(description="Script to dump all UPnP information's of a given host.")
parser.add_argument("host", type=str, help="the host to get all UPnP information's from")
parser.add_argument("-t", "--timeout", type=str, help="timeout for network actions in seconds", default=1)
parser.add_argument("-u", "--user", type=str, help="username for authentication", default="")
parser.add_argument("-p", "--password", type=str, help="password for authentication", default="")
parser.add_argument("--http", type=str, help="proxy URL for http requests (http://proxyhost:port)", default="")
parser.add_argument("--https", type=str, help="proxy URL for https requests (https://proxyhost:port)", default="")

parser.parse_args()
args = parser.parse_args()

#######################################################################################################################

use_timeout = args.timeout
use_host = args.host
use_user = args.user
use_pw = args.password
use_httpProxy = args.http
use_httpsProxy = args.https

#######################################################################################################################

# setup proxies for discovery call
proxies = {}
if use_httpsProxy:
    proxies = {"https": use_httpsProxy}

if use_httpProxy:
    proxies = {"http": use_httpProxy}

# get TR64 multicast result for the given host to get XML definition url
result = Discover.discoverParticularHost(use_host, proxies=proxies, timeout=use_timeout)

if not result:
    raise ValueError("Could not discover given host: " + use_host)

# get instance of device
box = DeviceTR64.createFromURL(result.location)
box.username = use_user
box.password = use_pw
box.httpProxy = use_httpProxy
box.httpsProxy = use_httpsProxy

# the discovery result contains the right URL to initialize device definitions
box.loadDeviceDefinitions(result.location, timeout=use_timeout)
# load the actions
box.loadSCPD(timeout=use_timeout, ignoreFailures=True)

device = {"informations": box.deviceInformations, "services": {}}

if len(box.deviceInformationUnknownKeys.keys()):
    device["unknownKeys"] = box.deviceInformationUnknownKeys

# merge the informations
for service in box.deviceServiceDefinitions.keys():
    device["services"][service] = copy.copy(box.deviceServiceDefinitions[service])

    if service in box.deviceSCPD.keys():
        # noinspection PyTypeChecker
        device["services"][service]["actions"] = box.deviceSCPD[service]  # the type checker is right, this is dirty

# print it out in a formated way
print(json.dumps(device, indent=4, sort_keys=True, separators=(',', ': ')))
