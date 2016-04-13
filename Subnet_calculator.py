   ####Subnet_calculator.py###Author##Mr.Professor####

        ###########Application Part - 1  ##############
import random
import os

def subnet_calc():
    try:
        print "\n"

        #Checking Ip address validity
        while True:
            ip_address = raw_input("Enter an IP address: ")

            #Checking octets
            a = ip_address.split(".")

            if (len(a)==4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[0]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                break

            else:
                print "Ip is INVALID....Try again...!!!"
                continue

        masks = [255,254,252,248,240,224,192,128,0]

        #Checking Subnet mask validity
        while True:
            subnet_mask = raw_input("Enter a subnet mask: ")

            #checking octets
            b = subnet_mask.split(".")

                
            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
                break

            else:
                print "Subnet mask is INVALID"
                continue

        ###########Application Part - 2 ##############
            # Algorithm for subnet identification

        mask_octets_padded = []
        mask_octets_decimal = subnet_mask.split(".")

        for octet_index in range(0, len(mask_octets_decimal)):

            binary_octet = bin(int(mask_octets_decimal[octet_index])).split("b")[1]

            if len(binary_octet) == 8:
                mask_octets_padded.append(binary_octet)
            elif len(binary_octet) <= 8:
                binary_octet_padded = binary_octet.zfill(8)
                mask_octets_padded.append(binary_octet_padded)

        #print mask_octets_padded

        decimal_mask = "".join(mask_octets_padded)

           
        #Counting the host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = decimal_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)
                
        #Obtaining wildcard mask
        wildcard_octets = []
        for w_octet in mask_octets_decimal:
            wild_octet = 255 - int(w_octet)
            wildcard_octets.append(str(wild_octet))

        wildcard_mask = ".".join(wildcard_octets)

        #print wildcard_mask
        
        ###########Application Part - 3 ##############

        #Converts IP into binary string

        ip_octets_padded = []
        ip_octets_decimal = ip_address.split(".")


        for octet_index in range(0, len(ip_octets_decimal)):

            binary_octet = bin(int(ip_octets_decimal[octet_index])).split("b")[1]

            if len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                ip_octets_padded.append(binary_octet_padded)
            else:
                ip_octets_paded.append(binary_octet)

        #print ip_octets_padded

        binary_ip = "".join(ip_octets_padded)

        #print binary_ip


        #Obtain the network address and broadcast address from the binary string
        
        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        #print network_address_binary

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" *no_of_zeros
        #print broadcast_address_binary

        #Converting binary to decimal NetworkAddress
        net_ip_octets = []
        for octet in range(0, len(network_address_binary), 8):
            net_ip_octet = network_address_binary[octet:octet+8]
            net_ip_octets.append(net_ip_octet)

        #print net_ip_octets
        net_ip_address = []
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        #print net_ip_octets

        network_address = ".".join(net_ip_address)
        #print network_address

        #Converting binary to decimal BroadcastAddress
        bst_ip_octets = []
        for octet in range(0, len(broadcast_address_binary), 8):
            bst_ip_octet = broadcast_address_binary[octet:octet+8]
            bst_ip_octets.append(bst_ip_octet)
        
        #print bst_ip_octets
        
        bst_ip_address = []
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))
            
        #print bst_ip_address

        broadcast_address = ".".join(bst_ip_address)
        #print broadcast_address

        #Results for selected IP/mask
        print "\n"
        print "Network address is: %s" % network_address
        print "Broadcast address is: %s" % broadcast_address
        print "Number of valid hosts per subnet: %s" % no_of_hosts
        print "Wildcard mask: %s" % wildcard_mask
        print "Mask bits: %s" % no_of_ones
        print "\n"

        ###########Application Part - 4 ##############
        #       Generating random ip addresses       #
        while True:
            generate = raw_input("Generate random ip address from subnet? (y/n)")
            
            if generate == "y":
                generated_ip = []
                
                #Obtain available IP address in range, based on the difference between octets in broadcast address and network address
                for indexb, oct_bst in enumerate(bst_ip_address):
                    #print indexb, oct_bst
                    for indexn, oct_net in enumerate(net_ip_address):
                        #print indexn, oct_net
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                #Add identical octets to the generated_ip list
                                generated_ip.append(oct_bst)
                            else:
                                #Generate random number(s) from within octet intervals and append to the list
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))
                
                #IP address generated from the subnet pool
                #print generated_ip
                y_iaddr = ".".join(generated_ip)
                #print y_iaddr
                
                print "Random IP address is: %s" % y_iaddr
                print "\n"
                continue
                
            else:
                print "Ok, bye!\n"
                break  


        
    except KeyboardInterrupt:
        print "\n\nProgram aborted by user.DumDum..\n"
        sys.exit()

subnet_calc()
