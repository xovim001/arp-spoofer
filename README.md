# arp-spoofer

  Overview:
  ========
arp-spoofer is an ARP poisoning tool which can replace the ARP table of the target machine and redirect the internet traffic through the attacker machine. In order to run this tool, your target must be in the same local network. After you run the tool, the MAC address of the target machine will be replaced by your attacker machine's MAC address and all the internet traffic browse by the target machine will be flown through the attacker machine. After quitting the program by CTR + C, the ARP table of the target machine will be restored immediately and the target machine will get back o it's normal position. 

Dependencies
========
 Python 2 and scapy module

##USAGE: 
Navigate to the folder and run the following command:

python arp-spoof.py  --target (target ip address) --gateway (gateway/router address)
                                               OR
python arp-spoof.py -t (target ip address) --gateway (gateway ip address)

optional arguments:
  -h, --help            show this help message and exit
  -t TARGETS, --targets TARGETS
                        comma-separated list of IP addresses
  --gateway GATEWAY
                        IP address of the gateway or router

Examples
========
python arp-spoof.py --target 192.168.1.100 --gateway 192.168.1.1

Bugs & Contact
==============
Feel free to mail me with any problem, bug, suggestions or fixes at:
Sazzad Ovi <ovisecret@gmail.com>
