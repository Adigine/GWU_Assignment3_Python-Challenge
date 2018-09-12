import os
import csv
import sys

csvpath = os.path.join("..", "..", "..", "..", "..", "gitlab", "GWARL201808DATA3", "03-Python", "Homework", "Instructions", "PyPoll", "Resources", "election_data.csv")

with open(csvpath, newline='') as csvfile:
    votes = csv.reader(csvfile, delimiter=',')
    header = next(votes, None)
    print(header)
    print("Election Results")
    print("-------------------------")

    # Defining rows and casting columns because I was getting null values
    vote = [[int(row[0]), row[1], row[2]] for row in votes]

    #total count of votes
    totalVotes = sum(1 for row in vote)
    print(f"Total votes: {totalVotes}")

    candidateList = []
    for row in vote:
        if row[2] not in candidateList:
            candidateList.append(row[2])
    print(candidateList)

    for candidate in candidateList:
        for row in vote:
            if row[2] == candidate:
                print(candidateList[x])




#Exporting output to txt
# sys.stdout = open('Financial_Analysis.txt', 'w')
# print(f"")
# sys.stdout.close()
