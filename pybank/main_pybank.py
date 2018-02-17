# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:58:10 2018

@author: jakec
"""

import os
import csv

row_list = []


csvpath = os.path.join('raw_data/budget_data_1.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        row_list.append(row)
        
    

file = os.path.join('raw_data/budget_data_2.csv')
    
with open(file, newline='') as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)  # Rewind.
    csvreader = csv.reader(file)
    if has_header:
        next(csvreader)  # Skip header row.
    
    for row in csvreader:
        row[0] = row[0][:4] + row[0][6:]
        row_list.append(row)
        
months = 0        
revenue = 0        
max_rev = 0
min_rev = 0
for item in row_list[1:]:
    months = months + 1
    revenue = revenue + int(item[1])
    if int(item[1]) > max_rev:
        max_date = item[0]
        max_rev = int(item[1])
    if int(item[1]) < min_rev:
        min_date = item[0]
        min_rev = int(item[1])
    
avg_revenue = round(revenue / months, )

print('')
print('Financial Analysis')
print('---------------')
print('Total Months: ' + str(months))
print('Total Revenue: ' + '$' + str(revenue))
print('Average Revenue Change: ' + '$' + str(avg_revenue))
print('Greatest Increase in Revenue: ' + max_date + ' ' + '($' + str(max_rev) + ')')
print('Greatest Decrease in Revenue: ' + min_date + ' ' + '($' + str(min_rev) + ')')

with open('pybank_output.txt', 'w') as f:
    print('', file=f)
    print('Financial Analysis', file=f)
    print('---------------', file=f)
    print('Total Months: ' + str(months), file=f)
    print('Total Revenue: ' + '$' + str(revenue), file=f)
    print('Average Revenue Change: ' + '$' + str(avg_revenue), file=f)
    print('Greatest Increase in Revenue: ' + max_date + ' ' + '($' + str(max_rev) + ')', file=f)
    print('Greatest Decrease in Revenue: ' + min_date + ' ' + '($' + str(min_rev) + ')', file=f)
    






    
    
        
    

   

        