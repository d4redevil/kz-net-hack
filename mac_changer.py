import subprocess
import optparse
import re

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface",dest="interface",help="Specify the interface for changing the mac address")
    parser.add_option("-m","--mac",dest="mac",help="Specify a New Mac Address (00:00:00:00:00:00)")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-] Specify a interface to change its mac address for eg: wlan0, eth0")
    if not options.mac:
        parser.error("[-] Specify a new MAC address for eg: 00:00:00:00:00:00")
    return options
def mac_changer(interface,mac):
    subprocess.call(["ifconfig", interface,"down"])
    subprocess.call(["ifconfig", interface,"hw","ether",mac])
    subprocess.call(["ifconfig", interface,"up"])
def current_mac_address(interface):
    call_result=subprocess.check_output(["ifconfig",interface],universal_newlines=True)
    current_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", call_result)
    return current_mac.group(0)
def check_program(old,new):
    if not old == new:
        print("Mac address is Success fully changed to :",new)
    elif old==new:
        print("Try Using another Mac address")
    else:
        print("Mac Is not changed , Retry Later")
options=get_arguments()
Original_mac=current_mac_address(options.interface)
print("[-]The Original Mac Address is :"+ Original_mac)
mac_changer(options.interface,options.mac)
new_mac=current_mac_address(options.interface)
check_program(Original_mac,new_mac)

