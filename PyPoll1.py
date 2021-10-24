import os
import csv
# assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# assign a variable save the file to a
#  path
file_to_save = os.path.join("analysis", "election_analysis.txt")

results_dict = {"counties_dict": {}, "candidate_dict": {}   }
# open election results and read the file
with open(file_to_load) as election_data:
    # read the file object with the reader function
    file_reader=csv.reader(election_data)

    # define header row
    headers=next(file_reader)

    for row in election_data:
        print(row)

    









with open(file_to_save,"w") as txt_file:
