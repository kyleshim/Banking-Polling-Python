# Create a null list and add to list if the value is not in it yet by row
# Maybe a dictionary will contain all of the row values

import os
import csv

#Path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Read in csv file: budget_data.csv
with open(csvpath) as csvfile:

    # Split data at delimiter ","
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header in data
    header = next(csvreader)

    # Build a list of candidates
    unique_list = []
    total_list = []
    # Candidate dictionary
    candidates = {}
    total_votes = 0
    for row in csvreader:
        if row[2] not in unique_list:
            unique_list.append(row[2])
        total_list.append(row[2])    
        total_votes = total_votes+1
    #print(total_list)
    #for row in csvreader:
    #    for name in unique_list:
    #    candidates[row] = candidates.get(row,0)+1
    for name in total_list:
        if name in candidates:
            candidates[name] = candidates[name]+1
        else:
            candidates[name]=1
    votes_list=[candidates['Khan'],candidates['Correy'],candidates['Li'],candidates["O'Tooley"]]
    print(f'{votes_list}')
    print("Election Results")
    print("----------------")     
    print(f"Total Votes: {total_votes}") 
    print("----------------")
    print(f'{unique_list[0]} : {candidates[unique_list[0]]}')     
    print(f'{unique_list[1]} : {candidates[unique_list[1]]}')  
    print(f'{unique_list[2]} : {candidates[unique_list[2]]}')  
    print(f'{unique_list[3]} : {candidates[unique_list[3]]}')
    print("----------------")
    print(f'Winner: ')
    print("----------------")

    #print(unique_list)
    #print(candidates)

#    for row in csvreader:
#        if row[2] == candidates["name"][0]:
#            candidates["votes"].append(row[3])
    
#    print(candidates)
#    counter = int(0)
#    name = str(0)
#    for row in csvreader:
#        for name in unique_list:
#            if row[2] == name:
#                counter =+ 1

#    print(counter)

#    dummy = ["Harry", "Hermione", "Harry", "Ron", "Albus", "Sirius", "Albus"]
#    unique_set = set(dummy)
 #   candidates["votes"].append(unique_set)
#    print(unique_set)
#    print(candidates)
#        for name in candidates:

        # for row in csv->for name in unique_list: add to variable if =
