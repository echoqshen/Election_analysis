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

# initialise a total vote counter
total_votes=0

# candidate options
candidate_options=[]
# declear an empty dictionary
candidate_votes={}

# open election results
with open(file_to_load) as election_data:
    # to do: read and analyse the data here
    file_reader=csv.reader(election_data)
    
    # read the header row
    headers=next(file_reader)
    # print each row in the CSV file
    for row in file_reader:
        # add to total vote count
        total_votes +=1
        # print out candidate name from each row
        candidate_name=row[2]        
        # if candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add candidate name to candidate option list
            candidate_options.append(candidate_name)
            # 2. begin tracking candidate's vote count
            candidate_votes[candidate_name]=0
            # increment count for each candidate
        candidate_votes[candidate_name]+=1

    # % of votes/candidate
    # 1. 
    ### SEANS CODE BLOCK 
    print("canditate votes")
    print(candidate_votes)

    winning_vote_count = 0
    winner = ""
    total_number_votes = 0
    for (key) in candidate_votes:

        print(key)
        print(candidate_votes[key])
        # if this candidates votes are the highest, reset highest amount 
        if candidate_votes[key] > winning_vote_count:
            winning_vote_count = candidate_votes[key]
            # store the name of the winning candidate
            winner = key
    ### SEANS CODE BLOCK ENDS   

    for candidate_name in candidate_votes:
        # retrieve counts per candidate
        votes = candidate_votes[candidate_name]
        # calculate %
        vote_percentage = float(votes/total_votes) * 100
        # print out candidate name and % votes
        # print(f"{candidate_name}  gets {vote_percentage} % of votes  ")

        # Winning Candidate and Winning Count Tracker
        winning_candidate = ""
        winning_count=0
        winning_percentage = 0
        
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
             # To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
        print("here")
        print(f"{candidate_name} : {vote_percentage:.1f} % ({ votes }) \n")
        winning_candidate_summary=(
            f"----------------------------------------------------------\n" 
            f"winner: {winning_candidate} \n"
            f"winning vote count: {winning_count}\n"
            f"Winning percentage: {winning_percentage: .1f}%\n  "
            f"----------------------------------------------------------\n")
        print(winning_candidate_summary)
    # print out candidate list
    # print(candidate_votes)
    
    
    
# 3. print out total votes
# print(total_votes)

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

