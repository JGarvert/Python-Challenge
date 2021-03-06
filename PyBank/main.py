# Modules
import os
import csv
import locale

# "import" csv file and set file path
bud_data_path = os.path.join("","Resources","budget_data.csv")

# read csv file
with open(bud_data_path, 'r', newline="") as bud_data:
    csv_reader = csv.reader(bud_data, delimiter=",")
    csv_header = next(csv_reader)

    # count rows and sum profits.  Note that the original data file included a last row that was null.  I deleted it.
    row_count = 1
    first_row = next(csv_reader)
    profit_total = int(first_row[1])
    total_changes = 0
    previous_row = int(first_row[1])
    change_list = []
    change_date = []
    
    for row in csv_reader:
        row_count +=  1
        profit_total = profit_total + int(row[1])
        change = int(row[1]) - previous_row
        total_changes = change + total_changes
        previous_row = int(row[1])
        change_list.append(change)
        change_date.append(row[0])

    avg_change = total_changes/(row_count-1)
    max_change = max(change_list)        
    min_change = min(change_list)
        
    max_index = change_list.index(max(change_list))
    max_index_date = change_date[max_index] 
    min_index = change_list.index(min(change_list))
    min_index_date = change_date[min_index]

    # print to terminal.

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {row_count}")
    print("Total Profit/loss: $", format(profit_total, ",.2f"))
    print(f"Average Change: $", format(avg_change,",.2f"))
    print(f"Greatest increase in profits: {max_index_date} $({max(change_list)})")
    print(f"Greatest decrease in profits: {min_index_date} $({min(change_list)})")
   
    # print results to text file.
textfile_path = os.path.join("","Analysis","Budget_Analysis.txt") 
with open(textfile_path,'w') as text:
    text.write("Financial Analysis\n")
    text.write("---------------------------\n")
    text.write(f"Total Months: {row_count}\n")
    text.write(f"Total Profit/loss: $ {profit_total:.0f}\n")
    text.write(f"Average Change: $ {avg_change:.2f}\n")
    text.write(f"Greatest increase in profits: {max_index_date} $({max(change_list)})\n")
    text.write(f"Greatest decrease in profits: {max_index_date} $({min(change_list)})")