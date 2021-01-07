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
    print(csv_header)
    csv_firstrow = next(csv_reader)
    print(csv_firstrow)
    # # the below lines work
    # # lines = file_handler.read()
    # # print(lines)
    # # print(type(lines))

    # # count rows and sum profits then subtract 1 from row as last row is null
    # row_count = 0
    # profit_total = 0
    # for row in bud_data:
    #     row_count = row_count + 1
    #     profit_total = profit_total + "amount in [1]"
    
    # row_count = row_count - 1
     
    # # count charges and sum charges, then calculations
    # total_months = 0
    # total_charges = 0
    # for row in bud_data:
    #     if "amount in [1]" < 0
    #         total_months = total_months+ 1
    #         total_charges = total_charges+ "amount in [1]"

    # charges_avg = charges_total / charges_count

    # # format charges
    # # testing currency in print statement.....total_charges = local.currency(total_charges)
    # charges_avg = local.currency(charges_avg)
    
    # # greatest increase and decrease with  date and amount
    # large_inc_date = "[0] of row 1"
    # large_inc_profit = "[1] of row 1"
    # large_dec_date = "[0] of row 1"
    # large_dec_profit = "[1] of row 1"

    # for row in bud_data:
    #     if("[1] of that row " > large_inc_profit):
    #         large_inc_date = "[0] of that row"
    #         large_inc_profit = "[1] of that row"
    # for row in bud_data:
    #      if("[1] of that row " < large_inc_profit):
    #         large_dec_date = "[0] of that row"
    #         large_dec_profit = "[1] of that row"

    # # print to terminal
    # print("Financial Analysis")
    # print("---------------------------")
    # print(f"Total Months: {total_months}")
    # print("Total Profit/loss: $", format(total_charges, ",.2f"))
    # print(f"Average Change: {charges_avg}")"
    # print(f"Greatest increase in profits: {large_in_date} (${large_inc_profit})")
    # print(f"Greatest decrease in profits: {large_dec_date} (${large_dec_profit})")

    # # print out results
    # output_path = os.path.join("","Analysi","budget_data.csv")
    # # csvwriter = csv.writer(["Total Months","Total Profit/Lose","Avergae charges","Date of greatest increase in profit","Greatest increase in profit","Date of greastes decrease in profit","Greatest decrease in profit"])
    # # csvwriter = csv.writer({total_months},{total_charges},{charges_avg},{large_inc_date},{large_inc_profit},{large_dec_date},{large_dec_profit})
    # file_object.write(str1)
    # file_object.writelines(l) for L = ["Total Months","Total Profit/Lose","Avergae charges","Date of greatest increase in profit","Greatest increase in profit","Date of greastes decrease in profit","Greatest decrease in profit"]
    # file_object.write(str2)
    # file_object.writelines(2) for M = [{total_months},{total_charges},{charges_avg},{large_inc_date},{large_inc_profit},{large_dec_date},{large_dec_profit}]