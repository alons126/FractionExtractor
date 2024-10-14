import os
import re

def extract_integer_from_file(filepath):
    # Open the file and read its contents
    with open(filepath, 'r') as file:
        for line in file:
            # Search for the line that starts with the desired string
            if line.startswith("#(events) w/ exactly 1e:"):
                # Use a regex to capture the integer after any whitespace
                match = re.search(r'#\(events\) w/ exactly 1e:\s+(\d+)', line)
                if match:
                    return int(match.group(1))  # Return the captured integer
    return None  # Return None if the line was not found

def process_directories(base_directory):
    results = []
    # Loop through all directories in the base directory
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith(".txt"):  # Check if the file is a txt file
                filepath = os.path.join(root, file)
                integer_value = extract_integer_from_file(filepath)
                if integer_value is not None:
                    results.append((file, integer_value))

    # Sort results by filename
    results.sort(key=lambda x: x[0])

    # Print the sorted results
    for file, integer_value in results:
        print(f"File: {file}, Integer: {integer_value}")


# Example usage
base_directory = "/Users/alon/Downloads/Ar40_simulation_SuSa_Q2_6GeV_S01ACwoChi2_ChainRunV5_R2"  # Change this to your base directory path
process_directories(base_directory)