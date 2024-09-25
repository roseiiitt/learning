import scapy.all as scapy
import argparse

def get_arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target")
    options=parser.parse_args()
    return options

def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    answered_list=scapy.srp(arp_request_broadcast,timeout=1, verbose=False)[0]

    clients_list=[]
    for elemnts in answered_list:
        clients_dict={"ip":elemnts[1].psrc,"mac":elemnts[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_results(result_lists):
    print("IP\t\t","Mac Address","\n-----------------------------------")
    for client in result_lists:
        print(client["ip"] + "\t" + client["mac"])

options=get_arguments()
lists=scan(options.target)
print_results(lists)
