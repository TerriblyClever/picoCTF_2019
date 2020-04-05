#!/usr/bin/env python3
from scapy.all import *

pcap = rdpcap("capture.pcap") #read in the pcap data to an object, pcap

flag = ""
for packet in pcap[UDP]: #loop through all UDP packets (as seen in Wireshark initial analysis)
	try:
	#	packet[IP].show() #if the UDP packet has an IP field, show it
		if packet[IP].src == "10.0.0.2" and packet[IP].dst == "10.0.0.12":
			flag += packet[Raw].load.decode("utf-8") #.decode("ASCII") would work as well
			#print(packet[Raw].load) #initial test to see output of 'load'
	except IndexError:
		continue #otherwise skip that particular packet
		
print(flag)
