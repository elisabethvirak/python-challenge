import csv
import os

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
    data = next(csvfile)
    prev_net = data[1]
    print(prev_net)

    for row in csv_reader:
        print(int(row[1]))
        print(prev_net)
