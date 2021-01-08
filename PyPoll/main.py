# Modules
import os
import csv
import locale

# "import" csv file and set file path
elec_data_path = os.path.join("","Resources","election_data.csv")

# read csv file
with open(elec_data_path, 'r', newline="") as elec_data:
    csv_reader = csv.reader(elec_data, delimiter=",")
    csv_header = next(csv_reader)
    # # this is a test to view the data
    # print(csv_header)
    # csv_firstrow = next(csv_reader)
    # print(csv_firstrow)

    # count number of rows and sum total counts
    total_vote = 0
    Num_rows = 0
    for row in elec_data:
        Num_rows = Num_rows + 1
        total_vote = total_vote + int(total_vote[2])
    Num_rows = Num_rows - 1

    # Make list of unique candidates,
    candidates = {"Candidate": "", "VoteCount": int(0), "Pct": int(0)"}
    for row in [1,Num_rows]:
        if elec_data[2] <> elec_data[2] - 1
            candidates.append(elec_data[Candidate)
        else:
            candidates


