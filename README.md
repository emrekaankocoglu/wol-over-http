# wol-over-http
Setting up a Wake-on-LAN packet distribution network to use Wake-on-LAN behind CGNAT/Firewalls
## DISCLAIMER
This project is more of a proof-of-concept and NOT READY FOR DEPLOYMENT. Although it covers most, unexpected inputs and outputs are not filtered in places which can result in remote code execution on either multicasting server or WOL packet distributor clients. Cryptographic comparisons may also leak timing information.
## Why?
With individual IPv4 addressing getting more and more difficult as the number of users rapidly increase, ISP's go in the way of connecting users through the same IPv4 address using Carrier-Grade NAT. This makes accessing home networks nearly impossible as there are no inbound ports directly accessible behind a NAT bridge.
With this approach, we "punch" a hole in the home networks through a HTTP server to make communication with home networks possible, and with the use of an always-on client in the home network (an RPi or even a Python-capable UNIX-based router will work if requisites are met), we can send WOL packets inside the home network easily.
## How?
A sample diagram is shown below. We initialize an HTTP and Socket.io server outside of these networks which we will call the main server. Then, we have always-on packet distributor clients inside home networks which are always in connection with the main server. WOL targets are initialized with commands on these distributors as well since they have access to those. A outside client can connect to the main server via HTTP on port 80 ,which is guaranteed not to be blocked in order to maintain Internet access, and make the main server send the appropriate packets.
## Deploy
A web-server that is capable of PHP should serve the file index.php (nginx, Apache2). send.py and multicast_client.py files should be in the same directory with index.php with appropriate execution permissions for the web-server user. mac_server.py should be always running on the same server as a service -directory does not matter-, and the same applies to wol_client-server.py, only the execution should be on distributor clients inside the home network and after the main server. Adding and removing clients are described in Distributor Client section. 
## Outside Client
Type the URL, select the computer with the MAC address you want to wake and the key to do so.
## Distributor Client-Servers
-to be described-
### Usage
```
python3 wol_client-server.py <ip-address-of-main-server> <change> <change-mac-addr> <change-key> <change-label>
```
  By default, only the IP address of the main server is required. But if a change is needed, one can use <change> argument as -add or -remove and enter the attributes afterwards.
  
  Add or remove operations are only made here as they apply to the main server as well.
  
  pairs.txt should be present in the same folder as wol_client-server.py to maintain previously added addresses and keys at every start.
## Main Server
-to be described-
Execute mac_server.py with no arguments.
## To do
-Security on PHP side will get deployment-ready with measures to prevent injection attacks etc.  
-Inputs will be verified to further increase the overall security.  
-Callback mechanisms will be implemented on the distributor side to ensure the data is processed correctly.  
-Auto-deploy bash script on server side will be made
  





