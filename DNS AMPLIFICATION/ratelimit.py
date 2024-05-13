from scapy.all import *
from collections import defaultdict
import time

MAX_CONNECTIONS_PER_SECOND = 5
WINDOW_SIZE = 1  # Time window in seconds

# Dictionary to store IP records
ip_records = defaultdict(lambda: {'timestamps': [], 'count': 0})


def is_rate_limited(ip):
    current_time = time.time()

    # Check if IP record exists
    if ip in ip_records:
        # Count the number of connections within the time window
        count = sum(1 for t in ip_records[ip]['timestamps'] if current_time - t <= WINDOW_SIZE)

        # If the count exceeds the maximum connections per second, return True (rate limited)
        if count >= MAX_CONNECTIONS_PER_SECOND:
            return True
        # Otherwise, update the timestamp and return False (not rate limited)
        else:
            ip_records[ip]['timestamps'].append(current_time)
            ip_records[ip]['count'] += 1
            return False
    else:
        # IP record not found, create a new one
        ip_records[ip]['timestamps'].append(current_time)
        ip_records[ip]['count'] = 1
        return False


# Packet handler function
def packet_handler(pkt):
    if IP in pkt:
        source_ip = pkt[IP].src

        # Check if the source IP address is rate limited
        if is_rate_limited(source_ip):
            print("Rate limited:", source_ip)
            # Implement your response for rate-limited IP addresses here
        else:
            print("Processing request from:", source_ip)
            # Implement your normal response logic here


# Sniff packets and call packet_handler function for each packet
sniff(filter="ip", prn=packet_handler)
