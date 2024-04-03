import csv
import os

# Initialize a variable to store the total number of votes
total_votes = 0

# Path to the CSV file
file_path = os.path.join("Resources","budget_data.csv")

# Open the CSV file and read its contents
with open(file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv)
    
    # Skip the header row
    next(csv_reader)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Increment the total votes by 1 for each row
        total_votes += 1

# Print the total number of votes cast
print(f"Total Votes Cast: {total_votes}")
