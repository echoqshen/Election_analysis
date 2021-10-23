# 1. total numbers of votes
# 2. complete list of candidates
# 3. total votes per candidate
# 4. % votes/candidate
# 5. find out who won

import os
import csv

# direct path
# assign a variable for the file to load and the path.
# file_to_load='resources/election_results.csv'

# indirect path
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save=os.path.join("analysis", 'election_analysis.txt')
# print(file_to_load)
# open the election results and read the file
# election_data=open(file_to_load,'r') as one way to do it
with open(file_to_load) as election_data:
    # to do: read and analyse the data here
    file_reader=csv.reader(election_data)
    # print each row in the CSV file
    # for row in file_reader):
    #     print(row)

    # print the header row
    headers=next(file_reader)
    print(headers)

# create a filename variable to a direct/indirect path to the file
# file_to_save=os.path.join("analysis", "election_analysis.txt")
# using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save,"w")
# using the with statement open the file as a text file.
# with open(file_to_save,"w") as txt_file:
    # write 'hello world' to 'election_analysis.txt
    # txt_file.write("hello world")
    # write county names in place of 'hello world'
    # txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenvor\nJefferson")

