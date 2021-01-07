# Modules
import os
import csv

# "import" csv file and set file path
bud_data_path = os.path.join("","Resources","budget_data.csv")

with open(bud_data_path, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))