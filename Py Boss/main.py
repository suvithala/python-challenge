
import os
import csv
import datetime



# States Dictionary

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

employeefiles = ['1', '2']

# Create empty Lists

empid = []
Name = []
DOB = []
SSN = []
State = []

firstname = []
lastname = []
DOBformated = []
SSNformated = []
Stateabv = []


# Read from CSV file 

for filenumber in employeefiles:

	employeecsv = os.path.join('employee_data' + filenumber + '.csv')


	with open(employeecsv, newline="") as csvfile:

		csvreader = csv.reader(csvfile, delimiter=",")

		#skip headers

		next(csvreader, None)

		for row in csvreader:

			empid.append(row[0])
			Name.append(row[1])
			DOB.append(row[2])
			SSN.append(row[3])
			State.append(row[4])

			# Get First and Last Name

			new_name = row[1].split(" ")
			firstname.append(new_name[0])
			lastname.append(new_name[1])

			# Change DOB Format

			d = datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%m/%d/%Y")
			DOBformated.append(d)

			# Mask First five digits of SSN

			s = "*" * (len(row[3]) - 4) + row[3][-4:]
			SSNformated.append(s)

			# Get State abbreviations 

			for key, value in states.items():
				
				if row[4] == value:
					st = key
					Stateabv.append(st)	

# Create a Zip list

formatedCSV = zip(empid, firstname, lastname, DOBformated, SSNformated, Stateabv)

# Write to CSV File

newemployeedataCSV = os.path.join('EmployeedataFormated.csv')

with open(newemployeedataCSV, 'w', newline="") as csvFile:

	csvWriter = csv.writer(csvFile, delimiter=',')

    # Write Headers into file

	csvWriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write the zipped lists to a csv

	csvWriter.writerows(formatedCSV)


		
			

