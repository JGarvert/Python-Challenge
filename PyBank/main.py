#General psudo code
#import modulces, csv file, read in csv file delimited by comma with new line ?
#count # rows excluding header and last row that is null
#sum [1]
#count and sum charges over period. Divide for averate
#find max amount, with date and amount
#find min amount, with date and amount
#print to csv

# import modules
import os
import csv

# set path tried this because other things werrn't working
# path = "/PyBank/Resources"

# "import" csv file and set file path
bud_data_path = os.path.join("","Resources","budget_data.csv")


# read "imported" csv file as read only and split by commas and skip header
# with open(bud_data_path, newline='') as bud_data:
with open(bud_data_path, newline="") as bud_data:
    csvreader = csv.reader(bud_data, delimiter=",")
    csvheader = next(csvreader)
    
    # count rows and sum profits then subtract 1 from row as last row is null
    row_count = 0
    profit_total = 0
    for row in bud_data:
        row_count = row_count + 1
        profit_total = profit_total + "amount in [1]"
    
    row_count = row_count - 1
     
    # count charges and sum charges, then calculations
    charges_count = 0
    charges_total = 0
    for row in bud_data:
        if "amount in [1]" < 0
            charges_count = charges_count + 1
            charges_total = charges_total + "amount in [1]"

    charges_avg = charges_total / charges_count

    # greatest increase and decrease with  date and amount
    large_inc_date = "[0] of row 1"
    large_inc_profit = "[1] of row 1"
    large_dec_date = "[0] of row 1"
    large_dec_profit = "[1] of row 1"

    for row in bud_data:
        if("[1] of that row " > "[1] that row" )
        






