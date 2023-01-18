Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dependencies
... import csv
... import os
... 
... 
... 
... #files to load and output
... file_to_load = os.path.join(".", "Resources", "election_data.csv")
... file_to_output = os.path.join(".", "Analysis", "election_data_analysis.txt")
... 
... 
... # Total Vote Counter
... total_votes = 0
... 
... # Candidate Options and Vote Counters
... candidate_options = []
... candidate_votes = {}
... 
... # Winning Candidate and Winning Count Tracker
... winning_candidate = ""
... winning_count = 0
... 
... # Read the csv and convert it into a list
... with open(file_to_load) as election_data:
...     reader = csv.reader(election_data)
...     header= next(reader)
... 
...     # For each row...
...     for row in reader:
...         
...         # Add to the total vote count
...         total_votes = total_votes + 1
... 
...         # Extract the candidate name from each row
...         candidate_name = row[2]
...        
...         # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results)

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
