import scapy.all as scapy
def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast=arp_request/broadcast
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()

scan("192.168.1.1/24")
