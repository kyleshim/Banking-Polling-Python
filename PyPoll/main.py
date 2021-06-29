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

    # Candidate dictionary
    candidates = {"name": []}

    for row in csvreader:
        if row[2] not in unique_list:
            unique_list.append(row[2])
            candidates["name"].append(row[2])
        
    print(unique_list)
    print(candidates)