# import modules needed
import csv
import os

# create values
profit_loss = 0
months = 0 
monthly_profit_list = []
month_max_profit = ["", 0]
month_max_loss = ["", 0]
avg_profloss = 0

# create path to find csv file
budget_csv = os.path.join("budget_data.csv")

# create csvfile to write to
output = os.path.join("budget_data_final.txt")

# open csv file using csv reader
with open(budget_csv, 'r', newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # grab header file
    csv_header = next(csv_reader)
    print(f"Header:{csv_header}")

    # define values to compare to
    stats = next(csv_reader)
    prev_net = int(stats[1])
    # include Jan-2010 in count for months and profit_loss
    months = months + 1
    profit_loss = profit_loss + int(stats[1])
    
    # iterate through the rows
    for row in csv_reader:

        # find total profit_loss
        profit_loss = profit_loss + int(row[1])

        # add up months
        months = months + 1

        # set initial values to calculate monthly change
        monthly_change = int(row[1]) - prev_net
        # record monthly change to list
        monthly_profit_list.append('monthly_change')
        
        # find greatest increase in profits
        if (monthly_change > month_max_profit[1]):
            
            # store max profit value
            month_max_profit[1] = monthly_change

            # store month of max value
            month_max_profit[0] = str(row[0])
        
        # find greatest decrease in profits
        if (monthly_change < month_max_loss[1]):
            
            # store max loss value
            month_max_loss[1] = monthly_change

            # store month of max loss
            month_max_loss[0] = str(row[0])
        
        # reset prev_net
        prev_net = int(row[1])
    

    # format final table
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(profit_loss))
    print("Average Change: $" + str(avg_profloss))
    print("Greatest Increase in Profits: " + month_max_profit[0] + " ($" + str(month_max_profit[1]) + ")")
    print("Greatest Decrease in Profits: " + month_max_loss[0] + " ($" + str(month_max_loss[1]) + ")")
