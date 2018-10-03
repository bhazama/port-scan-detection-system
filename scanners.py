import os
import re

data_list = open("data/ssh.log.txt", "r")
#print(data_list) 

data = []
scan_count = 0
origin_ip = []
destination_ip = []

###reads through ssh.log.txt file and seperates into a list###
with data_list as reader:
    for line in reader:
        new_line = line.split()
        # ORIGIN IP: print(lines[2])
        # DESTINATION IP: print(lines[4]) 
        
        ### check length of line to see if it has origin/destination ip's ###
        if len(new_line) > 4:
            scan_count += 1
            ### checks if origin ip is already in logger ###
            if new_line[2] in origin_ip:
                continue
            else:
                origin_ip.append(new_line[2])

            ### checks if destination ip is already in logger ###
            if new_line[4] in destination_ip:
                continue
            else:
                destination_ip.append(new_line[4])

###testing variables###
#print("SCAN COUNT:" + str(scan_count))
#print("ORIGIN" + str(origin_ip))
#print("DESTINATION" + str(destination_ip))
#print(origin_ip)
#print(destination_ip)

### creating and opening scanners_found.txt file ###
scanners_found = open("scanners_found.txt", "w")
scanners_found.write("SCAN LOG \n\n")


### writing number of total scan attempts to logger file ###
scanners_found.write("[scan attempts] " + str(scan_count) + "\n")
scanners_found.write("\n\n[scan origin hosts]\n")

### loop through all origin ip's and write to logger file ###
for ip in origin_ip:
    scanners_found.write(ip + "\n")

### loop through destination ip's and write to logger file ###
scanners_found.write("\n\n[scan destination hosts]\n")

for ip in destination_ip:
    scanners_found.write(ip + "\n")

scanners_found.close()



        

