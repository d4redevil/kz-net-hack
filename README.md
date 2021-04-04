**kz-net-hack**
=

**kn-net-hack** is a Python based hacking tool. 

**kz-net-hack** is only compatible in Linux. 


**PYTHON SCRIPTS**
=

***ARP-SPOOFER***  - arp_spoofer.py help you to automate Reconnaissance Using NMAP and Helps you in finding your target. Once the target is found and chosen. 
It Will continuously spoof your target and Router Untill You interupt.

PREREQUISITE 
-

***NMAP SCANNER*** - To Perform Good Reconnaissance.

**Debian or ubuntu Based LINUX** 

```
sudo apt update && sudo apt install nmap
```

**RHEL, Fedora or Centos LINUX** 

```
sudo apt update && sudo yum install nmap
```

USAGE:
-

**Debian or ubuntu Based LINUX**

```
su -
sudo python3 arp_spoofer.py
```

**RHEL, Fedora or Centos LINUX** 

```
su -
sudo python3 arp_spoofer.py
```

NOTE: Make Sure you are in root user. Since IP Forward file has to be accessed.

------------------------------------------------

***MAC SPOOFER*** - A Mac spoofer which Works by passing Arguments. It can only support on linux.

PREREQUISITE
-

***Net-Tools*** - To Spoof Mac Address.


**Debian or ubuntu Based LINUX** 

```
sudo apt update && sudo apt install net-tools
```

**RHEL, Fedora or Centos LINUX**

```
sudo apt update && sudo yum install net-tools
```

USAGE:
-

```
sudo python3 macspoofer.py --interface INTERFACE --mac NEW_MAC 
```

#INTERFACE - specify the interface name to which you wanna change mac. Example:wlan0,eth0
#NEW_MAC - Specify a New Mac to spoof. Example: 00:00:00:00:00:00

For Help:
-

```
python3 macspoofer.py --help
```

NOTE:Make Sure that you use a Even number on the 1st OCTET & MAC ADDRESS is in COLEN-HEXADECIMAL-NOTATION

---------------------------------------------------

I tried my best to make The Code more readable. I'll Encourage Beginners to Read and Understand The Program.

**NOTE: This is only for educational purposes. The owner of this repository is not responsible for any kind of malicious activity performed with this tool.** 
