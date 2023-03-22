import json

# Prompt the user to enter a file name (without extension)
filename = input('Enter the name of the JSON file (without extension): ')

# Hard-code the file format as ".json"
file_path = f'{filename}.json'

# Load JSON data from file
with open(file_path) as f:
    data = json.load(f)

# Count the number of objects in the JSON file
num_objects = len(data)

print(f'The JSON file "{filename}.json" contains {num_objects} objects.')

# Print the last object in the JSON data
if num_objects > 0:
    last_object = data[-1]
    print(f'The last object in the JSON file is:\n{json.dumps(last_object, indent=2)}')
else:
    print('The JSON file is empty.')

