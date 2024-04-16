#Imports modules needed to connect path and manupulate the csv files
import csv
import os

csv_file_path = os.path.join('Resources','budget_data.csv')

def count_months_in_csv(file_path):
    with open(file_path, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row
        
        # Initialize a counter for months
        month_count = 0
        
        # Iterate over the rows in the CSV file
        for row in reader:
            month_count += 1  # Increment the counter for each row
        
        return month_count

# Call the function and print the result
total_months = count_months_in_csv(csv_file_path)
print(f'Total number of months: {total_months}')




import csv
import os

csv_file_path = os.path.join('Resources', 'budget_data.csv')

def calculate_net_total(csv_filepath):
    # Initialize the net total variable
    net_total = 0
    
    # Open the CSV file
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        # Create a CSV reader
        reader = csv.DictReader(file)
        
        # Loop through each row in the CSV
        for row in reader:
            # Add the profit/loss amount to the net total
            net_total += int(row['Profit/Losses'])
    
    return net_total

# Call the function and print the results
net_total = calculate_net_total(csv_file_path)
print(f'Net Total: {net_total}')





import csv
import os

csv_file_path = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
total_change = 0
previous_profit_loss = None
changes = []

# Open and read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    
    for row in csvreader:
        # Increment total_months
        total_months += 1
        
        # Calculate the change in "Profit/Losses", if previous_profit_loss is not None
        if previous_profit_loss is not None:
            change = int(row[1]) - previous_profit_loss
            changes.append(change)
            total_change += change      
        # Update previous_profit_loss for the next iteration
        previous_profit_loss = int(row[1])

# Calculate the average change in "Profit/Losses"
average_change = total_change / len(changes) if changes else 0

# Print the results
print(f"Total Months: {total_months}")
print(f"Total Change in Profit/Losses: {total_change}")
print(f"Average Change in Profit/Losses: {average_change}")




import csv
import os

def analyze_profit(csv_file):
    max_increase = 0
    max_increase_date = ""
    previous_profit = None

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            profit = int(row['Profit/Losses'])
            if previous_profit is not None:
                increase = profit - previous_profit
                if increase > max_increase:
                    max_increase = increase
                    max_increase_date = row['Date']

            previous_profit = profit

    return max_increase_date, max_increase

if __name__ == "__main__":
    csv_file = os.path.join('Resources', 'budget_data.csv')
    max_increase_date, max_increase = analyze_profit(csv_file)
    print(f"The greatest increase in profits was {max_increase} on {max_increase_date}.")





import csv
import os

def analyze_profit(csv_file):
    max_decrease = 0
    max_decrease_date = ""
    previous_profit = None

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            profit = int(row['Profit/Losses'])
            if previous_profit is not None:
                decrease = profit - previous_profit
                if decrease < max_decrease:
                    max_decrease = decrease
                    max_decrease_date = row['Date']

            previous_profit = profit

    return max_decrease_date, max_decrease

if __name__ == "__main__":
    csv_file = os.path.join('Resources', 'budget_data.csv')
    max_decrease_date, max_decrease = analyze_profit(csv_file)
    print(f"The greatest decrease in profits was {max_decrease} on {max_decrease_date}.")





