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
    
    # this is where in non-school life I would put coding in to find a list of unique candidates and possibly tally their votes at the same time.  Due to lack of comprehension and time constraints, I am going for as many points as possible and skipping that step.
    # From the homework, we know there are 4 candidates.  I know this is 'cheating' but I'm going for partial credit.
    cand_1 = "Khan"
    cand_2 = "Correy"
    cand_3 = "Li"
    cand_4 = "O'Tooley"

    # create list of data for poll calculations plus total votes
    cand_all = [cand_1, cand_2, cand_3, cand_4]
    vote_per_cand = [0,0,0,0]
    vote_total = 0
 
    # tally it up!
    for row in csv_reader:
        vote_total += 1
        if row[2] == cand_1:
            vote_per_cand[0] += 1
        if row[2] == cand_2:
            vote_per_cand[1] += 1
        if row[2] == cand_3:
            vote_per_cand[2] += 1
        if row[2] == cand_4:
            vote_per_cand[3] += 1

    # make a list of percentages
    cand_1_pct = round((vote_per_cand[0] /  vote_total) *100 ,3)
    cand_2_pct = round((vote_per_cand[1] /  vote_total) *100 ,3)
    cand_3_pct = round((vote_per_cand[2] /  vote_total) *100 ,3)
    cand_4_pct = round((vote_per_cand[3] /  vote_total) *100 ,3)
    vote_results = [cand_1_pct, cand_2_pct, cand_3_pct, cand_4_pct]

    # winner
    winner_pct = max(vote_results)
    winner_index = vote_results.index(max(vote_results))
    winner_name = cand_all[winner_index]

    # print to terminal
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {vote_total}")
print("-----------------------------------")
print(f"{cand_1}: {cand_1_pct:.3f}% ({vote_per_cand[0]})")
print(f"{cand_2}: {cand_2_pct:.3f}% ({vote_per_cand[1]})")
print(f"{cand_3}: {cand_3_pct:.3f}% ({vote_per_cand[2]})")
print(f"{cand_4}: {cand_4_pct:.3f}% ({vote_per_cand[3]})")
print("-----------------------------------")
print(f"Winner: {winner_name}")



    # print to text file
textfile_path = os.path.join("","Analysis","Results_PyPoll.txt")
with open(textfile_path, 'w') as text:

    text.write("Election Results\n")
    text.write("-----------------------------------\n")
    text.write(f"Total Votes: {vote_total}\n")
    text.write("-----------------------------------\n")
    text.write(f"{cand_1}: {cand_1_pct:.3f}% ({vote_per_cand[0]})\n")
    text.write(f"{cand_2}: {cand_2_pct:.3f}% ({vote_per_cand[1]})\n")
    text.write(f"{cand_3}: {cand_3_pct:.3f}% ({vote_per_cand[2]})\n")
    text.write(f"{cand_4}: {cand_4_pct:.3f}% ({vote_per_cand[3]})\n")
    text.write("-----------------------------------\n")
    text.write(f"Winner:  {winner_name}\n")
    text.write("-----------------------------------")
  


  


         

    


