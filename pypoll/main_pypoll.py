# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:19:49 2018

@author: jakec
"""

import os
import csv

row_list = []


csvpath = os.path.join('raw_data/election_data_1.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        row_list.append(row)
        


file = os.path.join('raw_data/election_data_2.csv')
    
with open(file, newline='') as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)  # Rewind.
    csvreader = csv.reader(file)
    if has_header:
        next(csvreader)  # Skip header row.
    
    for row in csvreader:
        row_list.append(row)
     
candidates = {}

for votes in row_list:
    
    if votes[2] not in candidates.keys():
        candidates[votes[2]] = 0
    if votes[2] in candidates.keys():
        candidates[votes[2]] = candidates[votes[2]] + 1
        
del candidates['Candidate']
      
max_vote = max(candidates.values())
max_keys = [k for k,v in candidates.items() if v == max_vote]

total = sum(candidates.values())

for k,v in candidates.items():
    count = v/total
    candidates[k] = [candidates[k], count]
    
print('')
print('Election Results')
print('---------------------------')
print('Total Votes: ' + str(total))
print('---------------------')
for k,v in candidates.items():
    print(k + ': ' + str("{:.1%}".format(v[1])) + ' (' + str(v[0]) + ')')
print('---------------------------')
print('Winner: ' + str(max_keys[0]))
print('---------------------------')
            
with open('pypoll_output.txt', 'w') as f:  
    print('', file=f)
    print('Election Results', file=f)
    print('---------------------------', file=f)
    print('Total Votes: ' + str(total), file=f)
    print('---------------------', file=f)
    for k,v in candidates.items():
        print(k + ': ' + str("{:.1%}".format(v[1])) + ' (' + str(v[0]) + ')', file=f)
    print('---------------------------', file=f)
    print('Winner: ' + str(max_keys[0]), file=f)
    print('---------------------------', file=f)
    
    
    

