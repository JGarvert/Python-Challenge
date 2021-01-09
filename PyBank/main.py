 Modules
import os
import csv
import locale

# "import" csv file and set file path
bud_data_path = os.path.join("","Resources","budget_data.csv")

# read csv file
with open(bud_data_path, 'r', newline="") as bud_data:
    csv_reader = csv.reader(bud_data, delimiter=",")
    csv_header = next(csv_reader)
    # this is a test to view the data
    # print(csv_header)
    # csv_firstrow = next(csv_reader)
    # print(csv_firstrow)

   
    # count rows and sum profits.  Note that the original data file included a last row that was null.  I deleted it.
    first_row = next(csv_reader)
    row_count = 1
    profit_total = int(first_row[1])
    previous_row = int(first_row[1])
    total_changes = 0
    change_list = []
    
    for row in csv_reader:
        row_count +=  1
        profit_total = profit_total + int(row[1])
        change = int(row[1]) - previous_row
        total_changes = change + total_changes
        previous_row = int(row[1])
        change_list.append(change)

    avg_change = total_changes/(row_count-1)
    max_change = max(change_list)
    min_change = min(change_list)

    # print to terminal. Does not include date for greatest inc/dec at this time.
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {row_count}")
    print("Total Profit/loss: $", format(profit_total, ",.2f"))
    print(f"Average Change: {total_changes/(row_count -1)}")
    print(f"Greatest increase in profits: $({max(change_list)})")
    print(f"Greatest decrease in profits: $({min(change_list)})")

    # print out results in text

    title = ["Total Months", "Total Profit/Loss","Average Change". "Increase", "Greatest Decrease"]
    results = [{row_count},{profit_total},{total_changes/(row_count)-1},{max(change_list)},{min(change_list)}]
