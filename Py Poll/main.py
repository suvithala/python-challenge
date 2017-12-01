import os
import csv


electionfiles = ['1', '2']

# Create empty Lists

voterid = []
county = []
candidate = []
candidatelist = []

# Read from CSV file 

for filenumber in electionfiles:
	electioncsv = os.path.join('election_data_' + filenumber + '.csv')

# Open a text file to write

	electionresults = open("ElectionResults.txt", "w")


	with open(electioncsv, newline="") as csvfile:
		csvreader = csv.reader(csvfile, delimiter=",")

		#skip headers
		next(csvreader, None)

		for row in csvreader:
			voterid.append(row[0])
			county.append(row[1])
			candidate.append(row[2])

# Calculate Total Votes

totalvotes = len(voterid)

# Write total number of votes to terminal and Write to text File

print("Election Results")
print("--------------------------------------")
print("Total Votes:" + str(totalvotes))
print("--------------------------------------")


electionresults.write("Election Results\n")
electionresults.write("--------------------------------------\n")
electionresults.write("Total Votes:" + str(totalvotes) +"\n")
electionresults.write("--------------------------------------\n")

# Get Candidates Names and count number and percentage of votes each candidate got

for x in candidate:
	if x not in candidatelist:
		candidatelist.append(x)

cname = []
cpercent = []


for x in range(len(candidatelist)):
	votes = 0
	
	for i in range(len(candidate)):
		
		if candidatelist[x] == candidate[i]:
			votes = votes + 1
			percentagevotes = round((votes/totalvotes) * 100, 00)

	# Write candidate names and percentage of votes for each candidate to terminal and text file

	print(candidatelist[x] + ": " + str(percentagevotes) + "%" + " (" + str(votes) + ")")

	electionresults.write(candidatelist[x] + ": " + str(percentagevotes) + "%" + " (" + str(votes) + ")\n")

	# Append candidates names and percentage of votes to the list and get winners name

	cname.append(candidatelist[x])
	cpercent.append(percentagevotes)	

winpercent = 0
winner = None

for j in range(len(cpercent)):
	if cpercent[j] > winpercent:
		winpercent = cpercent[j]
		winner = cname[j]

# Write winners name to terminal and text file

print("--------------------------------------")		
print( "Winner: " + winner)
print("--------------------------------------")	

electionresults.write("--------------------------------------\n")		
electionresults.write( "Winner: " + winner+"\n")
electionresults.write("--------------------------------------\n")		

# Close the text file

electionresults.close()
















		
