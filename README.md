=======
### Banking-Polling-Python
#### <i> An analysis of Banking Information and a Polling Station</i>

----------------------

**Description:**

I used Pyhton to analyze banking information and an election.

<b>Datasets used:</b>

* [Budget Data](PyBank/Resources/budget_data.csv)

* [Election Data](PyPoll/Resources/election_data.csv)

### Tools used:
----------------------

  - Python

### Analysis:
----------------------

Banking Analysis was as follows:

 - Total Months - found reading each row in csv
 - Total Profit - found by adding profit for each row in csv
 - Average Profit Change - Total Profit / Total Months
 - Greatest Increase in Profits - read through csv and replace if greater
 - Greatest Decrease in Profits - read through csv and replace if lesser

Election Analysis was as follows:

 - Total Votes - add 1 for each row in csv
 - Unique Candidates - append if not in dictionary
 - Candidate Votes - add 1 if csv row matches specific candidate, repeat
 - Percent Vote - divide candidate votes by total votes
 - Winner - candidate with the most votes

###  Data Visualization:
----------------------

![financial_analysis](PyBank/analysis/financial_analysis.txt)

![elections_results](PyBank/analysis/elections_results.txt)
