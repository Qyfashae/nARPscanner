#Network ARP Scanner

from scapy.all import * as sa 

interface = "eth0" #Change for your desire
ip_range = "0.0.0.0/24" #Change for your desire
broadcastMac = "ff:ff:ff:ff:ff:ff" #Change for your desire

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)
ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

for send, recieve in ans: 
	print(recieve.sprintf(r"%Ether.src% - %ARP.psrc%"))

