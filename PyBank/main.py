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
        if prev != 0: #avoiding treating first month as an increase from zero value
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
    aveChange = round(sumChange / (totalMonths-1), 2)
    print(f"Average  Change: ${aveChange}")

    #remaining console print
    print(f"Greatest Increase in Profits: {maxMonthIncr} (${maxIncrease})")
    print(f"Greatest Decrease in Profits: {maxMonthDecr} (${maxDecrease})")

#Exporting output to txt
with open('Financial_Analysis.txt', 'w', newline="") as filewriter:
    filewriter.write("Financial Analysis\n")
    filewriter.write("____________________________________\n")
    filewriter.write(f"Total Months: {totalMonths}\n")
    filewriter.write(f"Net Profit/Losses: ${netProfit}\n")
    filewriter.write(f"Average  Change: ${aveChange}\n")
    filewriter.write(f"Greatest Increase in Profits: {maxMonthIncr} (${maxIncrease})\n")
    filewriter.write(f"Greatest Decrease in Profits: {maxMonthDecr} (${maxDecrease})\n")
