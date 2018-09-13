import os
import csv

csvpath = os.path.join("..", "..", "..", "..", "..", "gitlab", "GWARL201808DATA3", "03-Python", "Homework", "Instructions", "PyPoll", "Resources", "election_data.csv")

with open(csvpath, newline='') as csvfile:
    votes = csv.reader(csvfile, delimiter=',')
    header = next(votes, None)
    #print(header)


    # Defining rows and casting columns because I was getting null values
    vote = [[int(row[0]), row[1], row[2]] for row in votes]

    #total count of votes
    totalVotes = sum(1 for row in vote)

    #generating candidate list
    candidateList = []
    for row in vote:
        if row[2] not in candidateList:
            candidateList.append(row[2])
    #print(candidateList)

    #setting loop and variables
    plurality = 0
    winner = None

    # creating an empty set so that i can append each candidate's result for print and export later
    candidates = []
    i = 0
    for candidate in candidateList:
        voteCount = 0

        #vote count/percentage per candidate
        for row in vote:
            if row[2] == candidate:
                voteCount += 1
        candidates.append(f"{candidate}: {round((voteCount / totalVotes) * 100, 4)}% ({voteCount})")
        i += 1

        #vote outcome with a 0.5% margin that would trigger a recount in a real world scenario
        if voteCount > (plurality + (plurality * 0.005)):
            plurality = voteCount
            recount = False
            winner = candidate
        elif voteCount < (plurality - (plurality * 0.005)):
            pass
        else:
            recount = True

print("Election Results")
print("-------------------------")
print(f"Total votes: {totalVotes}")
print("-------------------------")
for x in range(i):
    print(candidates[x])
print("-------------------------")
if recount == False:
    print(f"Winner: {winner}")
else:
    print("Recount necessary")
print("-------------------------")

with open('Election_Results.txt', 'w') as filewriter:
    filewriter.write("Election Results\n")
    filewriter.write("-------------------------\n")
    filewriter.write(f"Total votes: {totalVotes}\n")
    filewriter.write("-------------------------\n")
    for x in range(i):
        filewriter.write(f"{candidates[x]}\n")
    filewriter.write("-------------------------\n")
    if recount == False:
        filewriter.write(f"Winner: {winner}\n")
    else:
        filewriter.write("Recount necessary\n")
    filewriter.write("-------------------------\n")
