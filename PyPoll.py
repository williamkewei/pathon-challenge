# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
import os
import csv

# define varibales
total_count_vote=0
votes=[]
candidate_count=[]
unique_candidates=[]
percent=[]

filepath = os.path.join('resources','pypoll.csv')
with open(filepath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    csv_header= next(csvfile)
    for row in csv_reader:
    # count total number of votes
        total_count_vote=total_count_vote+1
    # append unique names to candidate list
    # https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
    # list of all votes
        votes.append(row[2])
# another loop populate candidates count with each vote
    for candidate in unique_candidates:
        candidate_count.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/total_count_vote*100,3))
# find the winner index position of max count in candidate_count
    winner = unique_candidates[candidate_count.index(max(candidate_count))]

print ("election results")
print ("---------------")
print (f"total votes:{total_count_vote}")
print ("---------------")
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}:{percent[i]}%{candidate_count[i]}")
print ("---------------")
print (f"winner:{winner}")
print ("---------------")
# pypoll = ("pypoll.txt")
polloutput =os.path.join("output",'pypoll.txt')
with open(polloutput, "w") as outfile:
    outfile.write('election results')
    outfile.write('\n---------------')
    outfile.write(f"\ntotal votes:{total_count_vote}")
    outfile.write('\n---------------')
    for i in range(len(unique_candidates)):
        outfile.write(f"\n{unique_candidates[i]}:{percent[i]}%{candidate_count[i]}")
    outfile.write('\n---------------')
    outfile.write(f"\nwinner:{winner}")
    outfile.write('\n---------------')

