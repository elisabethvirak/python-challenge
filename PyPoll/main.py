# import modules needed
import csv
import os
import operator

# create values
candidates = []
total_votes = 0
correy_votes = 0
khan_votes = 0
li_votes = 0
otooley_votes = 0
winner = ""
winning_votes = 0

# create path to find csv file
poll_csv = os.path.join("election_data.csv")

# open csv file using csv reader
with open(poll_csv, 'r', newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # grab header file
    csv_header = next(csvfile)

    # sort csv file by candidate names
    sortedpoll = sorted(csv_reader, key=operator.itemgetter(2))
    
    # collect candidates
    for row in sortedpoll:
        
        # count number of votes
        total_votes = total_votes + 1

        # find unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            
        # count votes for Correy
        if row[2] == "Correy":
            correy_votes = correy_votes + 1
            
        # count votes for Khan
        elif row[2] == "Khan":
            khan_votes = khan_votes + 1

        # count votes for Li
        elif row[2] == "Li":
            li_votes = li_votes + 1

        # count votes for O'Tooley
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
            
# calculate percent of votes for each candidate
correy_perc = (correy_votes/total_votes)*100
khan_perc = (khan_votes/total_votes)*100
li_perc = (li_votes/total_votes)*100
otooley_perc = (otooley_votes/total_votes)*100

# vote results store in dictionary
results = {
    "Correy":[correy_perc, correy_votes],
"Khan":[khan_perc,khan_votes],
"Li":[li_perc,li_votes],
"O'Tooley":[otooley_perc,otooley_votes]}
print(results)

# create election results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

# define winner dictionary for percentage and votes
# iterate through candidates in results dictionary
for candidate in results:
    # grab candidate vote counts
    vote = results.get(candidate)
    print(f" {candidate}: {vote[0]:.3f}% {vote[1]:,}")
    # compare candidate votes to winning votes
    if (vote[1] > winning_votes):
        winner = candidate
        winning_votes = vote[1]
# print(winner)

print(f"Election Winner is: {winner} {winning_votes:,}")
'''
winner = [0,0]
second = [0,0]
third = [0,0]
fourth = [0,0]

# sort candidates using dictionary
if results[correy][1] > results

Sort candidates based on total votes
if correy_perc > khan_perc:
    correy_perc = winner
    khan_perc = second
else:
    khan_perc = winner
    correy_perc = second
if li_perc > winner:
    second = third
    winner = second
    li_perc = winner
elif li_perc < second:
    li_perc = third
else:
    second = third
    li_perc = second
if otooley_perc > winner:
    third = fourth
    second = third
    winner = second
elif otooley_perc < winner and otooley_perc > second:
    third = fourth
    second = third
    otooley_perc = second
elif otooley_perc < second and > third:
    third = fourth
    otooley_perc = third
else:
    otooley_perc = fourth

print("First: " + str(winner) + "")
'''