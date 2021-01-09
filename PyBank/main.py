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
    max_change_date = first_row[0]
    min_change_date = first_row[0]
    
    for row in csv_reader:
        row_count +=  1
        profit_total = profit_total + int(row[1])
        change = int(row[1]) - previous_row
        total_changes = change + total_changes
        previous_row = int(row[1])
        change_list.append(change)
        if row[1] == max_change:
            max_change_date = row[0]
        elif min_change == row[1]:
            min_change_date = row[0]
        else:
            max_change_date = max_change_date
            min_change_date = min_change_date


    avg_change = total_changes/(row_count-1)
    max_change = max(change_list)
    min_change = min(change_list)

    # # This assumes the min and max cannot be on the same date.
    # for row in csv_reader:
    #     if row[1] == max_change:
    #         print({max_change})
    #     else:
    #         print("huh")
    #     #     max_change_date = row[0]
    #     # elif min_change == row[1]:
    #     #     min_change_date = row[0]
    #     # else:
    #         # max_change_date = max_change_date
            # min_change_date = min_change_date   

    # print to terminal. Does not include date for greatest inc/dec at this time.
    # print({max_change_date})
    # print({min_change_date})
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {row_count}")
    # print("Total Profit/loss: $", format(profit_total, ",.2f"))
    # print(f"Average Change: $", format(avg_change,",.2f"))
    # print(f"Greatest increase in profits: {max_change_date} $({max(change_list)})")
    # print(f"Greatest decrease in profits: {min_change_date} $({min(change_list)})")
  

    # print to text file
        # first set file path

        # final_file_path = os.path.join("../Analysis","budget_analysis.txt")
        # file1 = open(final_file_path,"w")

# with open("../PyBank/Analysis","a") as outputfile:
    print("Financial Analysis", file=open("Budget Analysis.txt","a"))
    print("---------------------------",file=open("Budget Analysis.txt","a"))
    print(f"Total Months: {row_count}",file=open("Budget Analysis.txt","a"))
    print("Total Profit/loss: $", format(profit_total, ",.2f"),file=open("Budget Analysis.txt","a"))
    print(f"Average Change: {total_changes/(row_count -1)}",file=open("Budget Analysis.txt","a"))
    print(f"Greatest increase in profits: $({max(change_list)})",file=open("Budget Analysis.txt","a"))
    print(f"Greatest decrease in profits: $({min(change_list)})",file=open("Budget Analysis.txt","a"))
