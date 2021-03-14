import subprocess as sp
import re

def nmap_scan(ip):
    final=[]
    output=sp.check_output(["sudo","nmap","-sn",ip],universal_newlines=True)
    print(output)
    #IP Re formula for +.+.+.+
    #MAC Re Formula \w\w:\w\w:\w\w:\w\w:\w\w:\w\w
    #Device found by mac \(\S.*\)\n
    ip_search=re.findall(r"for +.+.+.+",output)
    for i in range (len(ip_search)):
        ip_search[i]=ip_search[i].replace("for ","")
    mac_search=re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",output)
    device_search=re.findall(r"\(\S.*\)\n",output)
    for i in range (len(device_search)):
        device_search[i]=device_search[i][1:len(device_search[i])-2]
    for ip,mac,device in zip(ip_search,mac_search,device_search):
        result={}
        result["ip"]=ip
        result["mac"]=mac
        result["name"]=device
        final.append(result)
        
        
    return final
if __name__=="__main__":
    scan_result=nmap_scan("192.168.1.1/24")#str(input("> enter IP / IP Range : ")))
    print(len(scan_result))
    for i in range(len(scan_result)):
        print("hello")
        if scan_result[i]["ip"] == "192.168.1.1":
            print(scan_result[i])
            print(f"-----ROUTER-----\nIP address : {scan_result[i]['ip']}\nMac Address:{scan_result[i]['mac']}\nDevice Name:{scan_result[i]['name']}")
            print("hi")
        if scan_result[i]["ip"] == "192.168.1.2":
            print(scan_result[i])
            print(f"-----Victim-----\nIP address : {scan_result[i]['ip']}\nMac Address:{scan_result[i]['mac']}\nDevice Name:{scan_result[i]['name']}")
        
    print(scan_result)
