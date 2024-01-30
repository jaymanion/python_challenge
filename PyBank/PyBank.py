import os

import csv

import math

csvpath = os.path.join('Resources', 'budget_data.csv')

#below is setting up all values needed
with open(csvpath) as fin:
    csv_reader = csv.reader(fin, delimiter = ";")
    headerline = next(fin)
    total = 0
    count = 0
    avg_change = 0
    first = 0
    last = 0
    prev = 0
    value_max = -math.inf
    value_min = math.inf

    #count, first, and prev are all used for Months, first value to calculate change, and prev to calculate increase and decrease)
    for row in csv.reader(fin):
        total += int(row[1])
        if count == 0:
            count += 1
            first = int(row[1])
            prev = int(row[1])
        #this loops through to calculate current value in the itteration plus the previous day to find greatest increase and decrease
        else:
            count += 1
            if (float(row[1]) - prev) > value_max:
                max_id, value_max = row[0], (float(row[1]) - prev)
             
                
            if (float(row[1]) - prev) < value_min:  
                min_id, value_min = row[0], (float(row[1]) - prev)
        
        #final place holders to find average change
        prev = int(row[1])        
        last = row[1]
        
value_max = int(value_max)
value_min = int(value_min)
avg_change = round((int(last) - int(first)) / (int(count) - 1), 2)
print("Financial Analysis")
print("----------------------------")
print (f'Total Months: {count}')
print (f'Total: {total}')
print (f'Average Change: ${avg_change}')
print (f'Greatest Increase in Profits: {max_id} (${value_max})')
print (f'Greatest Decrease in Profits: {min_id} (${value_min})')