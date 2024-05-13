from scapy.all import *
from random import getrandbits
    
dest_ip = "10.0.2.15"
dest_port = 80

ip = IP(src = "10.0.2.10", dst=dest_ip)

tcp=TCP(sport=RandShort(), dport=dest_port, flags="S", seq=100)

raw = Raw(b"Karthik")

p=ip/tcp/raw
srloop(p, verbose=0, inter=0.03)