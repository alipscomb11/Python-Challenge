import csv
import os

def count_votes(csv_file):
    total_votes = 0

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        total_votes = sum(1 for row in reader)

    return total_votes

if __name__ == "__main__":
    csv_file = os.path.join('Resources', 'election_data.csv')
    total_votes = count_votes(csv_file)
    print(f"Total votes cast: {total_votes}")





import csv
import os

def get_candidate_list(csv_file):
    candidate_list = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            candidate = row['Candidate']
            if candidate not in candidate_list:
                candidate_list.append(candidate)

    return candidate_list

if __name__ == "__main__":
    csv_file = os.path.join('Resources', 'election_data.csv')
    candidates = get_candidate_list(csv_file)
    print("List of candidates who received votes:")
    for candidate in candidates:
        print(candidate)




import csv
import os

def calculate_candidate_votes(csv_file):
    candidate_votes = {}

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        total_votes = sum(1 for row in reader)
        file.seek(0)  # Reset file pointer to the beginning
        for row in reader:
            candidate = row['Candidate']
            if candidate not in candidate_votes:
                candidate_votes[candidate] = 0
            candidate_votes[candidate] += 1

    return candidate_votes, total_votes

def calculate_percentage(candidate_votes, total_votes):
    percentage_dict = {}
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        percentage_dict[candidate] = percentage

    return percentage_dict

if __name__ == "__main__":
    csv_file = os.path.join('Resources', 'election_data.csv')
    candidate_votes, total_votes = calculate_candidate_votes(csv_file)
    percentages = calculate_percentage(candidate_votes, total_votes)
    
    print("Percentage of votes each candidate won:")
    for candidate, percentage in percentages.items():
        print(f"{candidate}: {percentage:.2f}%")




import csv
import os

def count_candidate_votes(csv_file):
    candidate_votes = {}

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            candidate = row['Candidate']
            if candidate not in candidate_votes:
                candidate_votes[candidate] = 0
            candidate_votes[candidate] += 1

    return candidate_votes

if __name__ == "__main__":
    csv_file = os.path.join('Resources', 'election_data.csv')
    candidate_votes = count_candidate_votes(csv_file)
    
    print("Total number of votes each candidate won:")
    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {votes}")





import csv
import os

def count_candidate_votes(csv_file):
    candidate_votes = {}

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            candidate = row['Candidate']
            if candidate not in candidate_votes:
                candidate_votes[candidate] = 0
            candidate_votes[candidate] += 1

    return candidate_votes

def find_winner(candidate_votes):
    winner = max(candidate_votes, key=candidate_votes.get)
    return winner

if __name__ == "__main__":
    csv_file = os.path.join('Resources', 'election_data.csv')
    candidate_votes = count_candidate_votes(csv_file)
    winner = find_winner(candidate_votes)
    
    print(f"The winner of the election is: {winner}")




