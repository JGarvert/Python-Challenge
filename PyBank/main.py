# import modules
import os
import csv

# "import" csv file and set file path
bud_data_csvpath = os.path.join("","Resources","budget_data.csv")

# read "imported" csv file as read only and split by commas and skip header
with open(bud_data_csvpath,"r") as bud_data:
    csv_reader = csv.reader(bud_data, delimiter=",")
    header = next(csv_reader)
