#!/usr/bin/env python3
from scapy.all import *

pcap = rdpcap("capture.pcap") #read in the pcap data to an object, pcap

flag = ""

for packet in pcap[UDP]: #loop through all UDP packets (as seen in Wireshark initial analysis)
    #packet.show() #test line to make sure pcap UDP packets could be rieviewed to see available fields

	try:
	#	packet[IP].show() #if the UDP packet has an IP field, show it
            if packet[IP].src == "10.0.0.66" and packet[IP].dst == "10.0.0.1":
                flag += chr(packet[UDP].sport-5000)
                #print(packet[UDP].sport) #test line to see if correct syntax for getting port number, WORKS

	except IndexError: #if the particular packet did not contain IP information
		continue #otherwise skip that particular packet
print(flag)
