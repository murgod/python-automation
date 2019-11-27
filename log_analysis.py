###############################################################################
#This script lists the hosts based on environment and append those hosts to splunk query
# 
#
###############################################################################
import os
import sys
import argparse
import arrow
from datetime import datetime

s1 = '10:33:26'
s2 = '11:15:49' # for example
FMT = '%H:%M:%S'

#twoSeconds = arrow.get('00:00:02', 'HH:mm:ss')
twoSeconds = datetime.strptime('00:00:02', FMT) - datetime.strptime('00:00:00', FMT)

threeSeconds = arrow.get('00:00:03', 'HH:mm:ss')

def time_diff(req_time, res_time):
    
    tdelta = datetime.strptime(res_time, FMT) - datetime.strptime(req_time, FMT) 
    req = arrow.get(req_time, 'HH:mm:ss')
    res = arrow.get(res_time, 'HH:mm:ss')
    duration = res - req
    print tdelta
    return tdelta

def cal_api_res_time(response):
    print response
    res = response.split(" ")
    print "INFO: Req time", res[1].split(",")[0]
    print "INFO: Res time", res[10]
    return time_diff(res[1].split(",")[0], res[10])

def checkForMatchingPattern(line, pattern): 
    if (line.find(pattern) == -1): 
        return False
    else: 
        return True

def analyse_apis(file):
    print "works fine"
    afile = open(file, "r")
    lines = afile.readlines() 
    print lines[1]
    for aline in range(len(lines)):
        if checkForMatchingPattern(lines[aline], "HTTP/1.1 200 OK"):
            print "INFO: Line no ", aline
            print lines[aline]
            date_n_time = lines[aline + 1]
            print date_n_time
            aline = aline + 14  #Once we find HTTP status 200 line, 14th line will contain the body.
            if checkForMatchingPattern(lines[aline], "updateMobileTransactionResponse"):
                print aline
                if cal_api_res_time(date_n_time) > twoSeconds:
                    print date_n_time
                    sys.exit()
                

            
 

parser = argparse.ArgumentParser(description='This script generates a PPS graph. Here is an example on how to '
                                             'call this script: python jmeter-analysis.py jmeter.log')

parser.add_argument('-infile', '--infile_name', help='Input file.', default=None)

args = parser.parse_args()

analyse_apis(args.infile_name)

