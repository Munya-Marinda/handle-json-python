import json

# Prompt the user to enter a file name (without extension)
filename = input('Enter the name of the JSON file (without extension): ')

# Hard-code the file format as ".json"
file_path = f'{filename}.json'

# Clear the contents of the JSON file
with open(file_path, 'w') as f:
    json.dump([], f)

print(f'The JSON file "{filename}.json" has been cleared.')

