# HTTP Flood Attack and Defense
## Introduction
HTTP Flood Attack is a type of DDoS attack designed to overwhelm and shut down a victim server by sending large volume of HTTP GET requests. HTTP Flood is a Layer 7 Attack that targets the server's resources, such as the memory and CPU. The main goal behind this type of attack is to overload the server CPU's ability to process incoming requests from legitimate users and to leave no space in the memory for new requests. 

## Setup
1. Set KaliLinux's processors to 4 CPUs with 100% execution cap and SeedUbuntu's processors to 2 CPUs with 35% execution cap.
2. Both VM machines must be connected to the same network for the attack to be successful, which is **"NAT Network"** for this tutorial. 
3. Run 3 terminal windows inside KaliLinux and enter into the location of where the attack code is stored.
4. The IP address of SeedUbuntu can be found using **"ifconfiq"** and the IP address will be defined in the HTTP Flood attack code inside of KaliLinux. In my case, the SeedUbuntu's IP address to be attacked is "10.0.2.4".
5. Inside SeedUbuntu, launch Apache2 by first installing apache2 in terminal with the command **"sudo apt-get install apache2"** and start the web server with **"sudo service apache2 start"**.
6. We then open up Firefox in SeedUbuntu and type in **"localhost/server-status"** and this is where we will be attacking and monitoring the status of the server during an attack.

## Attack & Result
Inside the 3 terminals of KaliLinux, enter in **"python3 http_flood_attack.py"** to run the attacks.
<img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/HTTP%20FLOOD%20ATTACK/KaliLinux_Terminal.png">

The Apache2 server can be monitored throughout different timestamps to best see the effect of HTTP Flood.

### Server Status before being attacked: (CPU Usage: idle, Requests: 0-1 being processed)
<img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/HTTP%20FLOOD%20ATTACK/Before_Attack.png"> 

### Server Status 15 seconds in: (CPU Usage: 8.87%, Requests: 30 being processed)
<img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/HTTP%20FLOOD%20ATTACK/Start_of_Attack.png">

### Server Status 2 minutes 34 seconds in: (CPU Usage: 17.1%, Requests: 143 being processed)
<img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/HTTP%20FLOOD%20ATTACK/Mid_Attack.png">

### Server Status 4 minutes 23 seconds in: (CPU Usage: 26.1%, Requests: 149 being processed)
<img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/HTTP%20FLOOD%20ATTACK/End_of_Attack.png">

As the attacker is sending in requests, the CPU load can be seen increasing in percentage over time, indicating that the HTTP GET requests are flooding and overwhelming the Apache2's server resources and ability to process the requests on time. 

## Defenses
**Apache2 mod_ratelimit**
Steps to Enable and Run mod_ratelimit (can be found on https://www.youtube.com/watch?v=dSd3axdGk_4&ab_channel=QuickNotepadTutorial)
1. Inside SeedUbuntu terminal, enter into root with **"sudo su"**.
2. Enable rate limit with **"a2enmod ratelimit"**
3. Next, we want to edit the conf file with **"gedit /etc/apache2/conf-available/ratelimit.conf"**
4. Enter the following inside the conf file:

   <img src="https://raw.githubusercontent.com/MrKarkeys/CS166Proj/main/HTTP%20FLOOD%20ATTACK/RATE_LIMIT_CONF.PNG">
   
6. Close out of editing and enter **"a2enconf ratelimit"** and you will be prompted to reload the service.

### Comparison of server status with mod_ratelimit on and off:
Without mod_ratelimit attacked by 4 terminals: 
