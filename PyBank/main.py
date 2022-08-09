# Import the os module
import os

# Module for reading CSV files
import csv

# Average calculation
from numpy import average

csvpath = 'Resources/budget_data.csv'

# Read the CSV file

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csvreader)

    # Create a dictionary to hold each row as a list including date and P&L
    PyBank = {}
    counter = 0

    # Read each row of data after the header and store in dictionary as lists
    for row in csvreader:
        PyBank[counter] = row
        counter += 1

# Set variables for Number of Months and Net Profit/Loss 
num_months = counter
p_l = 0

# Calculate Net P/L
for k,v in PyBank.items():
    p_l += float(v[1])

# Calculate changes in P/L and then the average of those changes
change_list = []

for k,v in PyBank.items():
    next_value = float(v[1])
    try:
        old_value = float(PyBank[k - 1][1])
    except:
        old_value = float(PyBank[0][1])
    change_list.append((next_value - old_value))

# Average of those changes
average_change = average(change_list)

# Set variables for greatest increase/decrease in profits
max_increase = 0
max_decrease = 0

# Calculate greatest increase/decrease in profits
for k,v in PyBank.items():
    if float(v[1]) > max_increase:
        max_increase = float(v[1])
        max_increase_period = v

for k,v in PyBank.items():
    if float(v[1]) < max_decrease:
        max_decrease = float(v[1])
        max_decrease_period = v

# Add print line for All Calculations and export to Text file
import sys

with open('report.txt', 'w') as f:
    for out in [sys.stdout, f]:
        print(f"""
Financial Analysis
----------------------------------
Total Months: {num_months}
Total: ${p_l:.0f}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {max_increase_period[0]} (${max_increase_period[1]})
Greatest Decrease in Profits: {max_decrease_period[0]} (${max_decrease_period[1]})
""", file = out)

# Move text file to Analysis
os.replace('../PyBank/report.txt','../PyBank/Analysis/report.txt') 