# HTTP Flood Attack and Defense
## Introduction
HTTP Flood Attack is a type of DDoS attack designed to overwhelm and shut down a victim server by sending large volume of HTTP GET requests. HTTP Flood is a Layer 7 Attack that targets the server's resources, such as the memory and CPU. The main goal behind this type of attack is to overload the server CPU's ability to process incoming requests from legitimate users and to leave no space in the memory for new requests. 

## Setup
1. Set KaliLinux's processors to 4 CPUs with 100% execution cap and SeedUbuntu's processors to 2 CPUs with 35% execution cap
2. Run 3 terminal windows inside KaliLinux and enter into the location of where the attack code is stored.
3. Inside SeedUbuntu, launch Apache2 by first installing apache2 in terminal with the command **"sudo apt-get install apache2"** and start the web server with **"sudo service apache2 start"**
4. We then open up Firefox in SeedUbuntu and type in **"localhost/server-status"** and this is where we will be attacking and monitoring the status of the server during an attack.
5. The IP address of SeedUbuntu can be found using **"ifconfiq"** and the IP address will be defined in the HTTP Flood attack code inside of KaliLinux. In my case, the SeedUbuntu's IP address to be attacked is "10.0.2.4".

## Attack & Result
1. 
## Defense
