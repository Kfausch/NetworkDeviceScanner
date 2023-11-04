from scapy.all import ARP, Ether, srp
from requests import get
import time


def scan(ip):
    # Create an ARP request packet to get the MAC address associated with the IP address
    arp_request = ARP(pdst=ip)

    # Create an Ethernet frame to wrap the ARP request
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine the Ethernet frame and ARP request
    arp_request_broadcast = broadcast / arp_request

    # Send the ARP request and receive the response
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    #MAC Vendor lookup api
    site = "https://api.macvendors.com/"

    devices = []

    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}

        mactoget = site + element[1].hwsrc
        vendor = get(mactoget).text
        #checks if there were errors in get request
        if "errors" in vendor:
            vendor = "Vendor not found"
        #slows script down so you do not exceed request limits
        time.sleep(2)
        device_info["type"] = vendor

        devices.append(device_info)

    return devices


def display_result(devices):
    print("IP Address\t\tMAC Address\t\tDevice Type")
    print("------------------------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t{device['mac']}\t{device['type']}")


if __name__ == "__main__":
    target_ip_range = "10.191.1.1/24"  # Change this to match your network range
    devices = scan(target_ip_range)
    display_result(devices)
