#
# Example:
# execute_action.py -u <username> -p <pw> http://192.168.178.1:49000/upnp/control/hosts
# urn:dslforum-org:service:Hosts:1 GetGenericHostEntry NewIndex::0
#
import os
import sys
import argparse
import requests
from simpletr64.devicetr64 import DeviceTR64

try:
    # noinspection PyCompatibility
    from urlparse import urlparse
except ImportError:
    # noinspection PyCompatibility,PyUnresolvedReferences
    from urllib.parse import urlparse

#######################################################################################################################

parser = argparse.ArgumentParser(description="Script to execute an UPnP action. \nExample is: " +
                                             os.path.basename(sys.argv[0]) +
                                             " -u <username> -p <pw> http://192.168.178.1:49000/upnp/control/hosts "
                                             "urn:dslforum-org:service:Hosts:1 GetGenericHostEntry NewIndex::0")
parser.add_argument("controlURL", type=str, help="the control URL which enables to call an action")
parser.add_argument("namespace", type=str, help="the namespace in which the actions resists")
parser.add_argument("action", type=str, help="the action to execute")
parser.add_argument("arguments", type=str, nargs="*",
                    help="argument(s) for the given action in the form: ArgumentName::Value")
parser.add_argument("-t", "--timeout", type=str, help="timeout for network actions in seconds", default=1)
parser.add_argument("-u", "--user", type=str, help="username for authentication", default="")
parser.add_argument("-p", "--password", type=str, help="password for authentication", default="")
parser.add_argument("--http", type=str, help="proxy URL for http requests (http://proxyhost:port)", default="")
parser.add_argument("--https", type=str, help="proxy URL for https requests (https://proxyhost:port)", default="")

parser.parse_args()
args = parser.parse_args()

#######################################################################################################################

use_controlURL = args.controlURL
use_namespace = args.namespace
use_action = args.action
use_timeout = args.timeout
use_user = args.user
use_pw = args.password
use_httpProxy = args.http
use_httpsProxy = args.https

use_arguments = {}

for argument in args.arguments:
    args = argument.split("::")

    if len(args) != 2:
        raise ValueError("Argument needs to be in the format of ArgumentName::Value, found: " + argument)

    use_arguments[args[0]] = args[1]

#######################################################################################################################

urlParts = urlparse(use_controlURL)
uri = urlParts.path

device = DeviceTR64.createFromURL(use_controlURL)

device.username = use_user
device.password = use_pw
device.httpProxy = use_httpProxy
device.httpsProxy = use_httpsProxy

try:
    # where the "magic" happens
    results = device.execute(uri, use_namespace, use_action, timeout=use_timeout, **use_arguments)
except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError) as e:
    print("Failed: " + str(e))
    results = {}

if len(results.keys()):
    print("Results:")

for resultKey in results.keys():
    if results[resultKey] is None:
        print(resultKey + "::")
    else:
        print(resultKey + "::" + results[resultKey])
