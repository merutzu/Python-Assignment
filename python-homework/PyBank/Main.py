# -*- coding: utf-8 -*-
"""Instructor Demo: CSV Reader.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, iterate over each
row of the file to capture employee salaries, calculate min,
max, avg metrics of employee salaries, and write the metrics
to a csv file.
"""

# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('../budget_data.csv')

# Initialize variable to hold profits and differences
profitloss = 0
profit = []
profit_diff = []
# Initialize line_num variable
line_num = 0
date = []
# Open the input path as a file object
with open(csvpath, 'r') as csvfile:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)
        line_num += 1
        profitloss += int(row[1])
        # Append the row profitloss value to the list of profits and losses
        #profitloss.append(profitloss)
        profit.append(int(row[1]))
        date.append(row[0])
        
    for i in range(1, len(profit)):
        profit_diff.append(profit[i] - profit[i-1])
        avg_profit_change = sum(profit_diff)/len(profit_diff)
        
        max_profit_change = max(profit_diff)
        min_profit_change = min(profit_diff)
        
        max_profit_date_change = str(date[profit_diff.index(max(profit_diff))+1])
        min_profit_date_change = str(date[profit_diff.index(min(profit_diff))+1])
        
print(f"Total Months: {line_num}")
print(f"Total $ {profitloss}")
print(f"average profit change is $ {avg_profit_change}")
print(f"Greatest increase in profit: {max_profit_date_change} ${max_profit_change}")
print(f"Greatest decrease in profit: {min_profit_date_change} ${min_profit_change}")

output_path = 'output.txt'
with open(output_path, 'w') as file:
    # Write daily_average to the output file, convert to string
    file.write((f"Total Months: {line_num}\n")
    file.write(f"Total $ {profitloss}\n”)
    file.write(f"average profit change is $ {avg_profit_change}\n")
    file.write(f"Greatest increase in profit: {max_profit_date_change} ${max_profit_change}\n")
    file.write(f"Greatest decrease in profit: {min_profit_date_change} ${min_profit_change}\n")
