import os
import csv
import locale

#Path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read in csv file: budget_data.csv
with open(csvpath) as csvfile:

    # Split data at delimiter ","
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header in data
    header = next(csvreader)
    
  
    totalprofit = float(0)
    greatestincrease = float(0)
    greatestdecrease = float(0)
    totalrows = int(0)
    # Loop through data rows
    for row in csvreader:
    
        netchange = float(row[1])

        totalprofit = float(totalprofit) + float(row[1])

        if float(row[1]) > float(greatestincrease):
            greatestincrease = float(row[1])
            increasemonth = row[0]
        elif float(row[1]) < float(greatestdecrease):
            greatestdecrease = float(row[1])
            decreasemonth = row[0]
    
        totalrows += 1

    averagechange = totalprofit/totalrows
    locale.setlocale(locale.LC_ALL, '')
    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months:{totalrows}")
    print(f"Total: {locale.currency(totalprofit, grouping=True)}")
    print(f"Average Change: {locale.currency(averagechange, grouping=True)}")
    print(f"Greatest Increase in Profits: {increasemonth} {locale.currency(greatestincrease, grouping=True)}")
    print(f"Greatest Decrease in Profits: {decreasemonth} {locale.currency(greatestdecrease, grouping=True)}")






# Total Months: Count of data rows w/o header
# Total Profit/Losses: Variable that is added or subtracted each row
# Average Change: Total Profit/ Months
# Greatest Increase: If Row[1] greater than greatest increase, also store Row[0] for increase
# Greatest Decrease: If Row[1] less than greatest decrease, also store row [0] for decrease