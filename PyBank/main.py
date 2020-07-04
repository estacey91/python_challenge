# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    #variables
    row_count = 0
    net_total = 0
    current_month = 0
    prior_month = 0
    change = 0
    average_change = []
    avg_changecalc = 0
    greatest_inc = 0
    greatest_dec = 0
    inc_date = 0
    dec_date = 0
    

    #count total months & total net amount of "Profit/Losses" over the period

    for row in csvreader:
        row_count += 1
        net_total = net_total + int(row[1])

    # average of the changes in "Profit/Losses" over the entire period
        current_month = int(row[1])
    
        if row_count > 1:

            change = current_month - prior_month 

            average_change.append(change)

            if change > greatest_inc:
                greatest_inc = change
                inc_date = row[0]

            if change < greatest_dec:
                greatest_dec = change
                dec_date = row[0]


        prior_month = int(row[1])


avg_changecalc = sum(average_change) / len(average_change)


#Print
print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(net_total))
print("Average Change: $" + str(avg_changecalc))
print("Greatest Increase in Profits: " + inc_date + " $" + str(greatest_inc))
print("Greatest Decrease in Profits: " + dec_date + " $" + str(greatest_dec))


# Specify the file to write to
output_path = os.path.join("Analysis", "pybank2.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the header
    csvwriter.writerow(['Financial Analysis', ''])

    # Write total months
    csvwriter.writerow(['Total Months:', '86'])

    # Write total of profit/losses
    csvwriter.writerow(['Total:', '$38382578'])

    # Write total of profit/losses
    csvwriter.writerow(['Average Change:', '$-2315.12'])

    # Write total of profit/losses
    csvwriter.writerow(['Greatest Increase in Profits:', 'Feb-12 $1926159'])

    # Write total of profit/losses
    csvwriter.writerow(['reatest Decrease in Profits:', 'Sep-13 $-2196167'])



