import scapy.all as scapy
def scan(ip):
    scapy.arping(ip,iface="en0")

scan("192.168.1.1/24")
