import subprocess as sp
import re


def nmap_scan(ip):
    final=[]
    
    #Scan using nmap
    output=sp.check_output(["sudo","nmap","-sn",ip],universal_newlines=True)
            
    #IP Re formula for +.+.+.+
    ip_search=re.findall(r"for +.+.+.+",output)
    
    #To remove unwanted string from results
    for i in range (len(ip_search)):
        ip_search[i]=ip_search[i].replace("for ","")
    
    #MAC Re Formula \w\w:\w\w:\w\w:\w\w:\w\w:\w\w
    mac_search=re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",output)

    #Device found by mac \(\S.*\)\n
    device_search=re.findall(r"\(\S.*\)\n",output)
    
    #To remove unwanted string from results
    for i in range (len(device_search)):
        device_search[i]=device_search[i][1:len(device_search[i])-2]
    
    #Ziping can remove unwanted string from search results
    for ip,mac,device in zip(ip_search,mac_search,device_search):
        result={}
        result["ip"]=ip
        result["mac"]=mac
        result["name"]=device
        final.append(result)
        
        
    return final




if __name__=="__main__":
    
    scan_result=nmap_scan(str(input("> enter IP / IP Range : ")))
    print(len(scan_result))
    
    #To list the information gathered
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
