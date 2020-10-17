# import modules
import csv
import os

# set variable for filepath
poll_data = os.path.join("PyPoll","csv.file","election_data.csv")

# set variables
total_votes = 0
candidate = ""
candidate_list = []
vote_list = []
percent_list =[]
winner = ""

# open csv file
with open (poll_data,'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # read the header
    header = next(csv_reader)
    
    # loop through each row in the csv file
    for row in csv_reader:
        #count the total number of votes
        total_votes = total_votes +1

        #s set condition to append lists
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1

# find vote percentage
percent_list = [(100/total_votes) * x for x in vote_list]

# find the winner
winner = candidate_list[vote_list.index(max(vote_list))]

# Print to terminal
print("Election results :")
print('--------------------------')
print(f'Total votes: {total_votes}')
for x in candidate_list:
    print(x + ": " + str(format(percent_list[candidate_list.index(x)], '.3f'))
        +"% (" + str(vote_list[candidate_list.index(x)]) +")")
print(f'Winner: {winner}')
print('--------------------------')

# export to a text file      
f = open("elections_analysis.txt","w")
f.write('--------------------------\n')
f.write("Election_results:\n")
f.write('--------------------------\n')
f.write(f'Total_votes:{total_votes}\n')
for x in candidate_list:
    f.write(x + ": " + str(format(percent_list[candidate_list.index(x)], '.3f'))
        +"% (" + str(vote_list[candidate_list.index(x)]) +")\n")
f.write('--------------------------\n')
f.write(f'Winner:{winner}\n')
f.write('--------------------------\n')
f.close()