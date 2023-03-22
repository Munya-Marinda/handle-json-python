import json

# Prompt the user to enter a file name (without extension)
filename = input('Enter the name of the JSON file (without extension): ')

# Hard-code the file format as ".json"
file_path = f'{filename}.json'

# Prompt the user to enter the number of last characters to read
num_chars = int(input('Enter the number of last characters to read: '))

# Read the last N characters of the JSON file
with open(file_path, 'rb') as f:
    f.seek(-num_chars, 2)
    last_chars = f.read().decode('utf-8')

# Print the last N characters to the console
print(f'The last {num_chars} characters of the JSON file "{filename}.json" are:\n{last_chars}')

