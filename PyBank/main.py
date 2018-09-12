import os
import csv
import sys

csvpath = os.path.join("..", "..", "..", "..", "..", "gitlab", "GWARL201808DATA3", "03-Python", "Homework", "Instructions", "PyBank", "Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    header = next(budget, None)
    #print(header)
    print("Financial Analysis")
    print("____________________________________")

    # Defining rows and casting column 2 as integers because I was getting zero values
    months = [[row[0], int(row[1])] for row in budget]
    #print(months)

    #getting count of Months
    totalMonths = sum(1 for row in months)
    print(f"Total Months: {totalMonths}")

    # Net profit/losses
    netProfit = sum(row[1] for row in months)
    print(f"Net Profit/Losses: ${netProfit}")

    #setting all parameters for loop
    prev = 0
    monthChange = 0
    sumChange = 0
    maxIncrease = 0
    maxDecrease = 0

    #Finding month to month change
    for row in months:
        if prev != 0:
            monthChange = row[1] - prev
        prev = row[1]

        # Max increase
        if monthChange > maxIncrease:
            maxIncrease = monthChange
            maxMonthIncr = row[0]

        # Max decrease
        if monthChange < maxDecrease:
            maxDecrease = monthChange
            maxMonthDecr = row[0]


        # sum change in profit/losses for calculating averae later
        sumChange += monthChange

    # Average change
    aveChange = sumChange / (totalMonths-1)
    print(f"Average  Change: ${aveChange}")

    #remaining console print
    print(f"Greatest Increase in Profits: {maxMonthIncr} (${maxIncrease})")
    print(f"Greatest Decrease in Profits: {maxMonthDecr} (${maxDecrease})")

#Exporting output to txt
sys.stdout = open('Financial_Analysis.txt', 'w')
print("Financial Analysis")
print("____________________________________")
print(f"Total Months: {totalMonths}")
print(f"Net Profit/Losses: ${netProfit}")
print(f"Average  Change: ${aveChange}")
print(f"Greatest Increase in Profits: {maxMonthIncr} (${maxIncrease})")
print(f"Greatest Decrease in Profits: {maxMonthDecr} (${maxDecrease})")
sys.stdout.close()
