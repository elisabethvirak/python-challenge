# import modules needed
import csv
import os

# create values
profit_loss = 0
months = 0 
monthly_profit_list = []
month_ref = []
avg_profloss = 0
max_profit = 0
max_loss = 0

# create path to find csv file
budget_csv = os.path.join("budget_data.csv")

# create csvfile to write to
output = os.path.join("budget_data_final.txt")

# open csv file using csv reader
with open(budget_csv, 'r', newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # grab header file
    csv_header = next(csvfile)
    print(f"Header:{csv_header}")

    # define values to compare to
    month = next(csvfile)
    prev_net = float(month[1])

    # iterate through the rows
    for row in csv_reader:
        
        # find total profit_loss
        profit_loss = profit_loss + int(row[1])

        # add up months
        months = months + 1

        prev_net = int(row)
        # set initial values to calculate monthly change
        monthly_change = int(row[1]) - prev_net
        # record monthly change to list
        monthly_profit_list.append('monthly_change')
        # keep track of source of monthly change
        month_ref.append(row[0])
        
        # find greatest increase in profits
        if monthly_change > max_profit:
            
            # store max profit value
            max_profit = monthly_change

            # store month of max value
            month_max_profit = str(row[0])
        
        # find greatest decrease in profits
        if monthly_change < max_loss:
            
            # store max loss value
            max_loss = monthly_change

            # store month of max loss
            month_max_loss = str(row[0])
    

    # format final table
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(profit_loss))
    print("Average Change: $" + str(avg_profloss))
    print("Greatest Increase in Profits: " + month_max_profit + " ($" + str(max_profit) + ")")
    print("Greatest Decrease in Profits: " + month_max_loss + " ($" + str(max_loss) + ")")


'''    # open new file to write data to
    with open(output, 'w', newline="") as datafile:
        csv_writer= csv.writer(datafile, delimiter=",")

        # write old csv file to new csv file
        for row in csv_reader:
            csv_writer.writerow(row)

            # append row for changes
            csv_writer.append(row)
    # open csvfile to write to
    with open(output, "w", newline="") as datafile:
        writer = csv.writer(output, delimiter=",")
        new_headers = csv_headers
        print(f"Header:{new_headers}")


'''
