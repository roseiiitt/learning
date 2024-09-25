import scapy.all as scapy
def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    answered_list=scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #in list
    print("IP\t\t","Mac Address","\n-----------------------------------")
    clients_lists=[]
    for i in  answered_list:
        clients_dict={"ip":i[1].psrc,"mac":i[1].hwsrc}
        clients_lists.append(clients_dict)
        print(i[1].psrc,"\t",i[1].hwsrc)
    print(clients_lists)

scan("192.168.1.1/24")