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
    
    # assign variables
    totalprofit = float(0)
    greatestincrease = float(0)
    greatestdecrease = float(0)
    totalmonths = int(0)

    # Loop through data rows
    for row in csvreader:
        

        # netchange = float(row[1]), used for testing

        # Add to total profit as each row progresses
        totalprofit = float(totalprofit) + float(row[1])

        # Determine the Greatest Profit increase and assign value if greater than previous
        if float(row[1]) > float(greatestincrease):
            greatestincrease = float(row[1])
            increasemonth = row[0]

        # Determine the Greatest Profit decreasr and assign value if greater than previous
        elif float(row[1]) < float(greatestdecrease):
            greatestdecrease = float(row[1])
            decreasemonth = row[0]

        # Count the number of months, assuming each row is new month
        totalmonths += 1
    # Calculate the average change
    averagechange = totalprofit/totalmonths

    #locale module used to format currency
    locale.setlocale(locale.LC_ALL, '')

    # Print results
    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months:{totalmonths}")
    print(f"Total: {locale.currency(totalprofit, grouping=True)}")
    print(f"Average Change: {locale.currency(averagechange, grouping=True)}")
    print(f"Greatest Increase in Profits: {increasemonth} ({locale.currency(greatestincrease, grouping=True)})")
    print(f"Greatest Decrease in Profits: {decreasemonth} ({locale.currency(greatestdecrease, grouping=True)})")


# Total Months: Count of data rows w/o header
# Total Profit/Losses: Variable that is added or subtracted each row
# Average Change: Total Profit/ Months
# Greatest Increase: If Row[1] greater than greatest increase, also store Row[0] for increase
# Greatest Decrease: If Row[1] less than greatest decrease, also store row [0] for decrease