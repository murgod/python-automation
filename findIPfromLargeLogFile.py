import collections
import heapq
import re

ipset = set()
prodcount = collections.defaultdict(int)
ipv4_pattern = re.compile("^(([01]?[0-9][0-9]?|25[0-5]|2[0-4][0-9]|)\\.){3}([01]?[0-9][0-9]?|25[0-5]|2[0-4][0-9]|)$")

file = open('weblog.txt', 'r')

for line in file:
    words = line.split()

    for word in words:
        if ipv4_pattern.match(word):
            print("valid IP:" +word)

            
