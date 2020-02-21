# import modules needed
import csv
import os

# create values
months = 0 
profit_loss = 0
avg_profloss = 0
max_profit = 0
max_loss = 0

# create path to find csv file
budget_csv = os.path.join("budget_data.csv")

# create csvfile to write to
output = os.path.join("budget_data_final.csv")

# open csv file using csv reader
with open(budget_csv, 'r', newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # open new file to write data to
    with open(output, 'w', newline="") as datafile:
        csv_writer= csv.writer(datafile, delimiter=",")

        # write old csv file to new csv file
        for row in csv_reader:
            csv_writer.writerow(row)

    # grab header file
    csv_header = next(csvfile)
    print(f"Header:{csv_header}")

    # iterate through the rows
    for row in csv_reader:

        # add up months
        months = months + 1

        # view profits/losses column as integer
        if int(row[1]) != 0:

            # calculate total profits/losses
            profit_loss = profit_loss + int(row[1])
        
        # find greatest increase in profits
        if int(row[1]) > max_profit:
            
            # store max profit value
            max_profit = int(row[1])

            # store month of max value
            month_max_profit = str(row[0])
        
        # find greatest decrease in profits
        if int(row[1]) < max_loss:
            
            # store max loss value
            max_loss = int(row[1])

            # store month of max loss
            month_max_loss = str(row[0])
    
    # open csvfile to write to
    with open(output, "w", newline="") as datafile:
        writer = csv.writer(output, delimiter=",")
        new_headers = csv_headers
        print(f"Header:{new_headers}")


    # format final table
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(profit_loss))
    print("Average Change: $" + str(avg_profloss))
    print("Greatest Increase in Profits: " + month_max_profit + " ($" + str(max_profit) + ")")
    print("Greatest Decrease in Profits: " + month_max_loss + " ($" + str(max_loss) + ")")
