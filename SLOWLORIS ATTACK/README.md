Example Slowloris Attack Code was taken from https://github.com/gkbrk/slowloris and is not included in this folder. 
===
This folder is a showcase of defenses created against the Slowloris attack for a project. There are two seperate approaches taken for this assignment: iptables and manual IP blocking.

Setup
---
For this specific setup, the VMs used are Kali Linux 6.6.9 64bit (10.0.2.6) as the attacker VM and SEEDUbuntu 16.04 (10.0.2.4) as the server host VM. The VMs were on their own NAT Network in VirtualBox. The server type we chose was Apache2, which allows us to create and use configuration files and modules for different uses. We tried to use mod_ratelimit, but it seemed ineffective for this specific attack type. The configuration files was used to create a blacklist against an IP found to be stalling connections within Wireshark manually. Beyond turning on our custom blacklist, Apache2 is not modified beyond adding installing apache2-utils and apache2-doc.

iptables
---
If you have iptables already installed in your distro, you can use this command in Terminal to limit the number of concurrent connections to 25 per IPv4 and reject connections beyond this:

sudo iptables -A INPUT -p tcp --syn --dport 80 -m connlimit --connlimit-above 25 --connlimit-mask 32 -j REJECT --reject-with tcp-reset

Screenshots are given of what occurs before and after running the iptables command in this same folder.


Manual IP blocking (Blacklist)
---
To determine what the attacker IP is, use Wireshark to see what connections are currently holding all the resources of the server.
The provided blacklist.conf file is the file we used to manually block the attacker VM's IP given the IP is not spoofed. Screenshots are provided to showcase what occurs. 
Note: The IP of the attacker VM in our instance was 10.0.2.6 but the attacker may have a different IP. In this instance, change the "Require not ip 10.0.2.6" line to the correct IP you intend to block. You can also add more than one ip by adding multiple lines of "Require not ip x.x.x.x".

Move the blacklist.conf file into the directory /etc/apache2/conf-available in order allow Apache2's commands to access the file.

To turn on the provided blacklist, use the Terminal and do:
sudo su
a2enmod blacklist
service apache2 reload

