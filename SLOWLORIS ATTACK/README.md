Example Slowloris Attack Code was taken from https://github.com/gkbrk/slowloris and is not included in this folder. 
===
This folder is a showcase of defenses created against the Slowloris attack for a project. There are two seperate approaches taken for this assignment: iptables and manual IP blocking.

Setup
---
For this specific setup, the VMs used are Kali Linux 6.6.9 64bit as the attacker VM and SEEDUbuntu 16.04 as the server host VM. The VMs were on their own NAT Network in VirtualBox. The server type we chose was Apache2, which allows us to create and use configuration files and modules for different uses. We tried to use mod_ratelimit, but it seemed ineffective for this specific attack type. The configuration files was used to create a blacklist against an IP found to be stalling connections within Wireshark manually. Beyond turning on our custom blacklist, Apache2 is not modified beyond adding installing apache2-utils and apache2-doc.

1. Install and run Kali Linux and SEEDUbuntu in a VM. This project uses VirtualBox. Make sure both VMs are on their own dedicated NatNetwork.
2. On Kali Linux, go to Terminal, make a directory, and run `git clone https://github.com/gkbrk/slowloris`
3. On SEEDUbuntu, install Apache2 and do systemctl start apache2 to run the server on SEEDUbuntu. 
4. On both SEEDUbuntu and Kali Linux, type `ifconfig` to see the IP addresses of the virtual machines. We will use these later to attack the SEEDUbuntu virtual machine.
   - To conifrm you can access the Apache2 server, type the IP address of SEEDUbuntu in the browser of Kali.
6. To run the attack, go to Kali and run `python3 slowloris.py IP_ADDRESS 500` and replace the IP_ADDRESS with your server IP. For this project, SEEDUbuntu had the IP address 10.0.2.4, so the code we run in Kali is `python3 slowloris.py 10.0.2.4 500`
7. Opening the website by typing SEEDUbuntu's IP address should be impossible as the website loads infinitely. To view what happens to the server as the attack runs, open Wireshark on SEEDUbuntu.
<a href="https://github.com/MrKarkeys/CS166Proj/blob/main/SLOWLORIS%20ATTACK/Slowloris%20Attack%20on%20Local%20VM.PNG"><img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/SLOWLORIS%20ATTACK/Slowloris%20Attack%20on%20Local%20VM.PNG"></a>

iptables
---
If you have iptables already installed in your distro, you can use this command in Terminal to limit the number of concurrent connections to 25 per IPv4 and reject connections beyond this:

`sudo iptables -A INPUT -p tcp --syn --dport 80 -m connlimit --connlimit-above 25 --connlimit-mask 32 -j REJECT --reject-with tcp-reset`

Screenshots are given of what occurs before and after running the iptables command in this same folder.

<a href="https://github.com/MrKarkeys/CS166Proj/blob/main/SLOWLORIS%20ATTACK/IPTables%20Defense.PNG"><img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/SLOWLORIS%20ATTACK/IPTables%20Defense.PNG"></a>

Manual IP blocking (Blacklist)
---
To determine what the attacker IP is, use Wireshark to see what connections are currently holding all the resources of the server.
The provided blacklist.conf file is the file we used to manually block the attacker VM's IP given the IP is not spoofed.
Note: The IP of the attacker VM in our instance was 10.0.2.6 but the attacker may have a different IP. In this instance, change the "Require not ip 10.0.2.6" line to the correct IP you intend to block. You can also add more than one ip by adding multiple lines of "Require not ip x.x.x.x".

Move the blacklist.conf file into the directory /etc/apache2/conf-available in order allow Apache2's commands to access the file.

To turn on the provided blacklist, use the Terminal and run the following commands in order:

`sudo su`

`a2enmod blacklist`

`service apache2 reload`

Screenshots are provided to showcase the difference. 

**Blacklist Off:**
<a href="https://github.com/MrKarkeys/CS166Proj/blob/main/SLOWLORIS%20ATTACK/Blacklist%20Off.PNG"><img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/SLOWLORIS%20ATTACK/Blacklist%20Off.PNG"></a>

**Blacklist On:**
<a href="https://github.com/MrKarkeys/CS166Proj/blob/main/SLOWLORIS%20ATTACK/Blacklist%20On.PNG"><img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/SLOWLORIS%20ATTACK/Blacklist%20On.PNG"></a>


