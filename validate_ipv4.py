import re
import sys

#Read command line input
IP = sys.argv[1]


#compile the regex to validate ipv4 address
ipv4_pattern = re.compile("^(([01]?[0-9][0-9]?)\\.){3}([01]?[0-9][0-9]?)$")


#check if IP matches all the rgex conditions
if  ipv4_pattern.match(IP):
    print "Valid ipv4 address"
else:
    print "invalid ipv4 address"


