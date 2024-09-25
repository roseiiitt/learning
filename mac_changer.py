import subprocess
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interfaces",dest="interfaces",help="Interface that you want to change the mac of")
    parser.add_option("-m","--mac",dest="mac",help="The mac address you want to set to")
    (options,arguments)=parser.parse_args()
    if not options.interfaces:
        parser.error("Please specify the interface you want to change mac address of")
    elif not options.mac:
        parser.error("Please specify the mac address")
    return options



def change_mac(interfaces,mac):
    print("The interfaces",interfaces,"mac address will be changed to",mac)
    subprocess.call(["sudo","ifconfig",interfaces,"down"])
    subprocess.call(["sudo","ifconfig",interfaces,"hw","ether",mac])
    subprocess.call(["sudo","ifconfig",interfaces,"up"])

options=get_arguments()
change_mac(options.interfaces,options.mac)

