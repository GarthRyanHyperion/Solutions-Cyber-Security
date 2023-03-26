import scapy.all as scapy
from scapy.all import *


packets = sniff(count=5)
print(packets[0], "0 printing ")
for packet in packets:
    print(packet[IP].src) #source
    print(packet[IP].dst) #destination

