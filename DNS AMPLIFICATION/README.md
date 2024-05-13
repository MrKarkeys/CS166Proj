# DNS Amplification Attack and Defense

## Overview
This repository contains information and code related to the implementation and defense against DNS Amplification attacks. DNS Amplification attacks leverage the characteristics of the DNS to flood a target network or server with an overwhelming volume of traffic, causing service disruption or downtime. This README provides details on how to execute the attack and implement a basic defense mechanism using rate limiting.

## Attack Setup
To execute the DNS Amplification attack, follow these steps:

1. Clone the repository containing the attack code from "rodarima" (link: https://github.com/rodarima/lsi/blob/master/p2/dnsdrdos.c).
2. Obtain public DNS server addresses from the internet and save them in a text file, with one address per line.
3. Place the text file containing DNS server addresses in the same directory as the attack code executable.
4. Compile the attack code with parameters specifying the target IP, number of packets, and DNS server domains.
5. If using a virtual environment like VirtualBox, initiate the attack from the attacker machine (in our case, SEEDUbuntu) to the target machine (in our case, Windows 10 virtual machine).
6. Obtain the IP address of the target machine (e.g., Windows 10) by running the "ipconfig" command in the command prompt.
7. Compile the attack code using `gcc` and create multiple executables (e.g., `dnsdrdos.o` and `dnsdrdos1.o`) to perform simultaneous attacks from the same virtual machine using different terminals.
8. Execute the attack by running the compiled code with appropriate parameters using the command `./dnsdrdos.o -f <filename> -s <Target IP> -l <loop count>`.

## Attack Result
Running the attack code floods the target machine with DNS responses, overwhelming the network and causing disruption. Observation of network utilization and packet reception can be done using tools like Wireshark.

![image](https://github.com/MrKarkeys/CS166Proj/assets/101848838/95e5efed-4ef4-4e74-ae5d-5da9b2aa9004)


## Defense Mechanism
To defend against DNS Amplification attacks, a basic rate limiting defense mechanism is implemented. This defense mechanism restricts the volume of incoming packets based on source IP addresses, thus mitigating the impact of such attacks. The defense code (`ratelimit.py`) utilizes Scapy for packet sniffing and manipulation.

### Implementation Steps
1. Install Scapy by executing `pip install scapy`.
2. Run the defense code using `sudo python ratelimit.py`.
3. The defense code sets the allowed number of packets/IP/sec to a default value of 5, which can be modified by editing the code.

![image](https://github.com/MrKarkeys/CS166Proj/assets/101848838/e5b30e02-4875-48c4-92af-040dac28e9a9)


## Analysis
DNS Amplification attacks are highly effective due to their ability to multiply the volume of data sent to the victim, causing network saturation and resource exhaustion. The use of spoofed IP addresses complicates mitigation efforts. Rate limiting serves as an effective defense mechanism by restricting the volume of responses a DNS server can send within a unit time, thus mitigating the impact of such attacks and conserving network bandwidth and resources.
