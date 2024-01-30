import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#below is setting up all values needed
with open(csvpath) as fin:
    csv_reader = csv.reader(fin, delimiter = ";")
    headerline = next(fin)
    count = 0
    charles = 0
    diana = 0
    raymon = 0
    win = 0

    #runs through itterations to properly count per person
    for row in csv.reader(fin):
        count += 1
        if 'Charles Casper Stockham' in row[2]:
            charles += 1
        if 'Diana DeGette' in row[2]:
            diana += 1
        if 'Raymon Anthony Doane' in row[2]:
            raymon += 1

#calculate the percentage of each person
charles_percent = round((charles/count)*100,3)
diana_percent = round((diana/count)*100,3)
raymon_percent = round((raymon/count)*100,3)

#finds who has the most votes and wins the election
largest = max(charles, diana, raymon)
   
if largest == charles:
        win = 'Charles Casper Stockham'
if largest == diana:
        win = 'Diana DeGette'
if largest == raymon:
        win = 'Raymon Anthony Doane'        
        
print("Election Results")
print("-------------------------")
print (f'Total Votes: {count}')
print("-------------------------")
print(f'Charles Casper Stockham: {charles_percent}% ({charles})')
print(f'Diana DeGette: {diana_percent}% ({diana})')
print(f'Raymon Anthony Doane: {raymon_percent}% ({raymon})')
print("-------------------------")
print(f'Winner: {win}')
print("-------------------------")