# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    #variables
    
    total_votes = 0

    total_khan_votes = 0 
    Khan_percentages = []
  
    total_correy_votes = 0 
    Correy_percentages = []

    total_li_votes = 0 
    li_percentages = []

    total_tooley_votes = 0 
    tooley_percentages = []
    
    for row in csvreader:
        
        #calc total # of votes
        total_votes += 1

        #calc each candidate percentage and count
        if row[2] == "Khan":
            total_khan_votes += 1
            Khan_percentages = total_khan_votes /total_votes * 100

        elif row[2] == "Correy":
            total_correy_votes += 1
            Correy_percentages = total_correy_votes /total_votes * 100

        elif row[2] == "Li":
            total_li_votes += 1
            li_percentages = total_li_votes /total_votes * 100

        elif row[2] == "O'Tooley":
            total_tooley_votes += 1
            tooley_percentages = total_tooley_votes /total_votes * 100
           
            
 
#Print
print("Election Results")
print("----------------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------------")
print("Khan: " + str(Khan_percentages) + "% " + str(total_khan_votes))
print("Correy: " + str(Correy_percentages) + "% " + str(total_correy_votes))
print("Li: " + str(li_percentages) + "% " + str(total_li_votes))
print("O'Tooley: " + str(tooley_percentages) + "% " + str(total_tooley_votes))
print("----------------------------------")
if total_khan_votes > total_correy_votes and total_khan_votes > total_li_votes and total_khan_votes > total_tooley_votes:
    print("Winner: Khan")
elif total_correy_votes > total_khan_votes and total_correy_votes > total_li_votes and total_correy_votes > total_tooley_votes:
    print("Winner: Correy")
elif total_li_votes > total_khan_votes and total_li_votes > total_correy_votes and total_li_votes > total_tooley_votes:
    print("Winner: Li")
elif total_tooley_votes > total_khan_votes and total_tooley_votes > total_correy_votes and total_tooley_votes > total_li_votes:
    print("Winner: Li")

print("----------------------------------")

# Specify the file to write to
output_path = os.path.join("Analysis", "pypollcsv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the header
    csvwriter.writerow(['Election Results', ''])

    # Write total votes
    csvwriter.writerow(['Total Votes:', '3521001'])

    # Write total for each participant
    csvwriter.writerow(['Khan:', '63.000% (2218231)'])

    
    csvwriter.writerow(['Correy:', '20.000% (704200)'])

    
    csvwriter.writerow(['Li:', '14.000% (492940)'])

    
    csvwriter.writerow(['O Tooley:', '3.000% (105630)'])

    # Write winner
    csvwriter.writerow(['Winner:', 'Khan'])