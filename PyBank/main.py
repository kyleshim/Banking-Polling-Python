import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')




# Total Months: Count of data rows w/o header
# Total Profit/Losses: Variable that is added or subtracted each row
# Average Change: Total Profit/ Months
# Greatest Increase: If Row[1] greater than greatest increase
# Greatest Decrease: If Row[1] less than greatest decrease