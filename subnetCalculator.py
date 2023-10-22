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

        # ----Checking Subnet Mask Validity----
        while True:
            subnet_mask = input("Enter subnet mask: ")
            mask_octets = subnet_mask.split(".")

            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            else:
                print("The Subnet Mask is INVALID! Please try Again .")
                continue

        # --Algorithm for Subnet indentification, based on IP and Subnet mask--
        
        mask_octets_binary = []
        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            mask_octets_binary.append(binary_octet.zfill(8))
        
        binary_mask = "".join(mask_octets_binary)

        no_of_zeros = binary_mask.count(0)
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2**no_of_zeros - 2)

        wildcard_octets = []
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))
        
        wildcard_mask = "".join(wildcard_octets)


    except:
        print('')