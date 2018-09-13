import os
import csv

#inserted state abbreviation Dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
EmpID = []
Last_Name = []
First_Name = []
DOB = []
SSN = []
State = []

csvpath = os.path.join("..", "..", "..", "..", "..", "gitlab", "GWARL201808DATA3", "03-Python", "Homework", "ExtraContent", "Instructions", "PyBoss", "employee_data.csv")

with open(csvpath, newline='') as csvfile:
    employees = csv.reader(csvfile, delimiter=',')
    header = next(employees, None)
    header[0] = 'EmpID'
    header.insert(1, "Last Name")
    header[2] = "First Name"
    print(header)

    # stateAbbrev = [sum(int(us_state_abbrev[dictvalue]) for dictvalue in listvalue.split()) for listvalue in employees[4]]

    for row in employees:

        #splitting name
        first,last = row[1].split(" ")
        row.insert(1, last)
        row[2] = first

        #DOB change
        year,month,day = row[3].split("-")
        row[3] = month + "/" + day + "/" + year

        #SSN anonymous
        ssn1,ssn2,ssn3 = row[4].split("-")
        row[4] = "***-**-" + ssn3

        #state abbreviation
        row[5] = us_state_abbrev[row[5]]

        EmpID.append(row[0])
        Last_Name.append(row[1])
        First_Name.append(row[2])
        DOB.append(row[3])
        SSN.append(row[4])
        State.append(row[5])

        print(row)
    print(header)

# zipping and writing new csv
revised_csv = zip(EmpID, Last_Name, First_Name, DOB, SSN, State)
output_file = os.path.join("employee_info_revised.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Employee ID', 'Last Name', 'First Name', 'DOB', 'SSN', 'State'])
    writer.writerows(revised_csv)
