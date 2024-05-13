
# Setup
1. Install Kali Linux on Virtual Box.
2. Install Ubuntu on Virtual Box.
3. Install Metasploitable.
4. Open and start up all VMs.
5. Make sure you can access the DVWA website by inputting Metsploitable's IP address into a web browser on Ubuntu.
6. Make sure syn cookies is disabled on metasploitable by running `cat /proc/sys/net/ipv4/tcp_syncookies`.
7. If the command outputs 0, syncookies is disabled. Good!
8. Now open up 3 terminals, wireshark, and system monitoring on Kali Linux

#Running the Attack
- This is how your setup should look before attacking Metsploitable.
![image](https://github.com/MrKarkeys/CS166Proj/assets/95559518/114a3f1e-f358-484e-be7c-c926054f1db2)

- One terminal will have our coded attack. This will be ran by writing `sudo python3 tcpsynflood.py` into command line.
- The other termianls will run `sudo hping3 -d 120 -S -p 80 --flood --rand-source (ip address of Metasploitable)`. This is done to help flood more SYN packets to our target. 
- -d 120 is the data size in bytes. -S means the SYN flag is enabled. -p 80 means you are attacking port 80. --flood means you are flooding the target. --rand-source randomizes the source IP address in the IP datagram. The last input is the IP address of your target, and in our case it is the Metasploitable VM.
- After running the attack in all the terminals, watch the packets in wireshark and your network usage using the Kali Linux system monitoring tool. 
![image](https://github.com/MrKarkeys/CS166Proj/assets/95559518/12ccb13d-ab65-4eba-a08b-74d45440175a)

- Now when reloading the DVWA web page, it will not reload and gets a soft lockup error on Metasploitable.
![image](https://github.com/MrKarkeys/CS166Proj/assets/95559518/04f6bba2-bfbe-4f9d-8395-b2e8f2f334c0)

- Now we are unable to connect and Metasploitable has crashed. 
![image](https://github.com/MrKarkeys/CS166Proj/assets/95559518/f9c67bd1-fcda-4b4b-8a9a-522f57adae62)

# References
- https://www.kali.org/tools/hping3/
- https://www.youtube.com/watch?v=1QNBrj58aCc
- CS166-L10-NetworkAttacks
