# NetworkDeviceScanner
Script that scans network using ARP and returns all IP's, MAC addresses, and uses a API to get the MAC vendor. 

This script is dependant on a few python libraries - Scapy, Requests, and Time.

Here are the steps you'll need to take on a new machine.
1. Install IDE - I am using Visual Studio Code
2. Download the latest version of Python from the Windows Store
3. Download/install the last version of npcap - I got it from https://npcap.com/#download
4. Install the Scapy and Request libraries from command promt
   pip install scapy
   pip install requests
5.Clone/copy the main.py script and run it

As of making this script, macvendors.com has limited use unless you register for a premium account
Free
1,000 requests/day
2 requests/second
