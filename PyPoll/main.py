# import os and csv modules
import os
import csv

# read the CSV file
csvpath = 'Resources/election_data.csv'

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvreader)

    # Create a dictionary to hold each row as a list
    PyPoll = {}
    counter = 0

    # Read each row of data after the header and store in dictionary as lists
    for row in csvreader:
        PyPoll[counter] = row
        counter += 1

# Set variables for Number of Votes and Candidate List
total_num_votes = counter
candidate_list = []

# Determine list of candidates
for k,v in PyPoll.items():
    candidate = v[2]
    if candidate not in candidate_list:
        candidate_list.append(candidate)

# Vote count for each candidate
first_vote_count = 0
second_vote_count = 0
third_vote_count = 0

# Determine total number of votes each candidate won and winner
for k,v in PyPoll.items():
    if candidate_list[0] == v[2]:
        first_vote_count += 1
    elif candidate_list[1] == v[2]:
        second_vote_count += 1
    elif candidate_list[2] == v[2]:
        third_vote_count += 1

vote_count_list = [first_vote_count, second_vote_count, third_vote_count]
max(vote_count_list)
winner = candidate_list[1]

# Determine the percentage of votes each candidate won
first_vote_percentage = (first_vote_count/total_num_votes)*100
second_vote_percentage = (second_vote_count/total_num_votes)*100
third_vote_percentage = (third_vote_count/total_num_votes)*100

vote_percentage_list = [first_vote_percentage, second_vote_percentage, third_vote_percentage]

# Add print line for Analysis and export to text file
import sys

with open('report.txt', 'w') as f:
    for out in [sys.stdout, f]:
        print(f"""
Election Results
------------------------------------------
Total Votes: {total_num_votes}
------------------------------------------
{candidate_list[0]}: {vote_percentage_list[0]:.3f}% ({vote_count_list[0]})
{candidate_list[1]}: {vote_percentage_list[1]:.3f}% ({vote_count_list[1]})
{candidate_list[2]}: {vote_percentage_list[2]:.3f}% ({vote_count_list[2]})
------------------------------------------
Winner = {winner}
""", file = out)

# Move text file to Analysis
os.replace('../PyPoll/report.txt','../PyPoll/Analysis/report.txt') 