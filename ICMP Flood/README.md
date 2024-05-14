Attack code used from https://github.com/antirez/hping and is not included in this folder.
===
This README is intended to guide users through an ICMP Flood attack for a project.

Setup
---
This example uses two virtual machines set up in VirtualBox. The virtual machines used are one Kali Linux VM and one SEEDLabs Ubuntu VM.

1. Install Virtual Box, the SEEDLabs Ubuntu VM, and the Kali Linux VM.
2. Attach both the Ubuntu and Kali VMs to NATNetwork in the Virtual Box Network settings for both VMs.
3. Launch the SEEDLabs VM and obtain its IP address through the `ifconfig` command in the terminal.
4. Open up System Monitor and Wireshark, both of which come preinstalled in the distribution.
5. Launch the Kali Linux VM.
6. Open the terminal and run the command `hping3 --icmp --flood <Target IP Address>` with the IP address of the SEEDLabs VM.
7. Observe the effects on Wireshark and System Monitor, or try opening a webpage to see the practical effects.
