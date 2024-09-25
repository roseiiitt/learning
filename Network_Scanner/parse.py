import scapy.all as scapy
def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    answered_list=scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #in list
    print("IP\t\t","Mac Address","\n-----------------------------------")
    for i in  answered_list:
        print(i[1].psrc,"\t",i[1].hwsrc)
   

scan("192.168.1.1/24")
