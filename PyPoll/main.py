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

    # Set a list of candidates votes and unique candidates
    unique_list = []
    total_list = []
    # Candidate dictionary to contain candidates name and votes
    candidates = {}
    # Set total votes to 0
    total_votes = 0
    winner_votes = 0
    # Prepare list for vote percentages
    vote_percent = []
    # Build out unique candidates list and count total votes
    for row in csvreader:
        if row[2] not in unique_list:
            unique_list.append(row[2])
        total_list.append(row[2])    
        total_votes = total_votes+1
    # Build out candidates dictionary
    for name in total_list:
        if name in candidates:
            candidates[name] = candidates[name]+1
        else:
            candidates[name]=1
    # Build candidates votes list         
    votes_list=[candidates['Khan'],candidates['Correy'],candidates['Li'],candidates["O'Tooley"]]
    # Build candidates percentage list
    for i in range(4):
        vote_percent.append((candidates[unique_list[i]]/total_votes)*100)
        if candidates[unique_list[i]] >= winner_votes:
            winner_votes = candidates[unique_list[i]]
            winner = unique_list[i]

    print("----------------")
    print("Election Results")
    print("----------------")     
    print(f"Total Votes: {total_votes}") 
    print("----------------")
    print(f'{unique_list[0]} : {str(round(vote_percent[0],4))} % ({candidates[unique_list[0]]})')     
    print(f'{unique_list[1]} : {str(round(vote_percent[1],4))} % ({candidates[unique_list[1]]})')  
    print(f'{unique_list[2]} : {str(round(vote_percent[2],4))} % ({candidates[unique_list[2]]})')  
    print(f'{unique_list[3]} : {str(round(vote_percent[3],4))} % ({candidates[unique_list[3]]})')
    print("----------------")
    print(f'Winner: {winner}')
    print("----------------")

     # Specify the file to write to
    output_path = os.path.join("analysis", "election_results.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as txtfile:
        output = ['Election Results', '-----------------']

        txtfile.writelines("Election Results")
        txtfile.writelines('\n')
        txtfile.write("----------------")
        txtfile.writelines('\n')
        txtfile.writelines(f"Total Votes: {total_votes}") 
        txtfile.writelines('\n')
        txtfile.write("----------------")
        txtfile.writelines('\n')
        txtfile.writelines(f'{unique_list[0]} : {str(round(vote_percent[0],4))} % ({candidates[unique_list[0]]})')
        txtfile.writelines('\n')
        txtfile.writelines(f'{unique_list[1]} : {str(round(vote_percent[1],4))} % ({candidates[unique_list[1]]})')  
        txtfile.writelines('\n')
        txtfile.writelines(f'{unique_list[2]} : {str(round(vote_percent[2],4))} % ({candidates[unique_list[2]]})') 
        txtfile.writelines('\n')
        txtfile.writelines(f'{unique_list[3]} : {str(round(vote_percent[3],4))} % ({candidates[unique_list[3]]})')
        txtfile.writelines('\n')
        txtfile.write("----------------")
        txtfile.writelines('\n')
        txtfile.write(f'Winner: {winner}')
        txtfile.writelines('\n')
        txtfile.write("----------------")