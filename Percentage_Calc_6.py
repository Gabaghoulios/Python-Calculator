
"""
Spyder Editor

This is a temporary script file.
"""

import re

def count_data(input_string):
    # Count of plus signs
    plus_count = len(re.findall(r'\+', input_string))
    
    # Count of letters (A-Z or a-z)
    letter_count = len(re.findall(r'[A-Za-z]', input_string))
    
    # Total number of characters
    total_count = len(input_string)
    
    # Return the counts and the total character count
    return plus_count, letter_count, total_count

def calculate_percentages(plus_count, letter_count, total_count):
    if total_count == 0:
        return 0, 0  # Avoid division by zero
    
    # Calculate percentages
    plus_percentage = (plus_count / total_count) * 100
    letter_percentage = ((letter_count + plus_count) / total_count) * 100
    
    return plus_percentage, letter_percentage

def process_data():
# Data input
    print("Enter data:")
    x = input()

# Get counts and total
    plus_count, letter_count, total_count = count_data(x)

# Calculate percentages
    plus_percentage, letter_percentage = calculate_percentages(plus_count, letter_count, total_count)

    print("Total characters:", total_count)
    print("Successful Independent Trials:", plus_count)
    print("Successful Cued Trials:", letter_count)
    print(letter_percentage, "% accuracy with cues", plus_percentage, "% accuracy independently")
    
    

def main():
    while True:
        try:
            process_data()
            
            # Ask user if they want to enter more data
            print("\nDo you want to enter more data? (yes/no)")
            user_input = input().strip().lower()

            if user_input != "yes":
                print("Goodbye!")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

#Create an if/then sequence or loop that prevents it from closing after each entry. 
#Maybe have it ask you if you want to input more data.  Yes/no. If yes, it does not close, else sys.exit
