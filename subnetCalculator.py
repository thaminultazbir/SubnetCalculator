import random
import sys

def subnetCalculator():
    try:
        print("\n")

        while True:
            ip_address = input("Input IP address: ")
            ip_octets = ip_address.split(".")

            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break

            else:
                print("Invalid IP address! Please retry")
                continue
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

    except:
        print('')