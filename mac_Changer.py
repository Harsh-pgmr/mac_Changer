#!/usr/bin/env python
#import subprocess and optparse
import subprocess
import optparse


def get_help():     #FUNCTION FOR CREATING PARSE OBJECTS 
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="iface", help="Interface to Change its Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter new Mac Address you like")
    (options, arguments) = parser.parse_args()
    if not options.iface:
        parser.error("Please Enter interface or type --help")
    elif not options.new_mac:
        parser.error("Please Enter New Mac Address or type --help")
    return options


def change_mac(iface, new_mac):     #FUNCTION FOR SYSTEM COMMANDS
    print(" [+]Mac Address for " + iface + " is changed to " + new_mac)
    subprocess.call(["ifconfig", iface, "down"])
    subprocess.call(["ifconfig", iface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", iface, "up"])

#CALIING change_mac AND get_help
options = get_help()
change_mac(options.iface, options.new_mac)
