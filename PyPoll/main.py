import os
import csv

#Call out the path to the intial data file

csv_path = os.path.join("Resources","election_data.csv")

#Call out the path for the file containin the calculated data

election_results_file = os.path.join("election_results.txt")

#Create dictionaries to store candidate's name, number of votes, and percentages

Candidate_Vote_Counts = {}

Candidate_Vote_Percentage = {}

# Set the intial value of total votes

Vote_Totals = 0

# Read the initial data file

with open(csv_path, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader) # Skip the header row
    
    # Work  through rows of data after the header
    
    for row in csvreader:
    
        Vote_Totals += 1
    
        Candidate = row[2]
        
        # Make sure candidate is in the dictionary
        
        if Candidate in Candidate_Vote_Counts:
            Candidate_Vote_Counts[Candidate] += 1
        else:
            Candidate_Vote_Counts[Candidate] = 1
    
    # Calculate and store candidate's vote percentage
    
    for Candidate in Candidate_Vote_Counts:
        Candidate_Vote_Percentage[Candidate] = round((Candidate_Vote_Counts[Candidate]/Vote_Totals)*100,3)
        
        print(round(Candidate_Vote_Percentage[Candidate], 3))
    
    # Find the winner by finding the candidate that has the highest vote count in the candidate_vote_counts dictionary.
    
    Winner = max(Candidate_Vote_Counts, key=Candidate_Vote_Counts.get)
    
    print(Winner)
    
    # Write the Summary table to a output file
    with open(election_results_file, "w") as resultfile:
        resultfile.write("\nElection Results\n")
        resultfile.write("\n-------------------------\n")
        resultfile.write(f"Total Votes: {Vote_Totals}\n")
        resultfile.write("\n-------------------------\n")
        for Candidate in Candidate_Vote_Counts:
            resultfile.write(f"{Candidate}: {Candidate_Vote_Percentage[Candidate]}% ({Candidate_Vote_Counts[Candidate]})\n")
        resultfile.write("\n-------------------------\n")
        resultfile.write(f"Winner: {Winner}")
        resultfile.write("\n-------------------------\n")