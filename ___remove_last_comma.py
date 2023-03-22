import json

# Prompt the user to enter a file name (without extension)
filename = input('Enter the name of the JSON file (without extension): ')

# Hard-code the file format as ".json"
file_path = f'{filename}.json'

# Read the contents of the file
with open(file_path, 'r') as f:
    content = f.read()

# Find the index of the last occurrence of "}" or "]"
last_bracket_idx = max(content.rfind('} , ]'), content.rfind('},]'))

# Remove the first occurrence of "} , ]" starting from the end of the file
new_content = content[:last_bracket_idx] + content[last_bracket_idx:].replace('}]', '', 1).replace('}]', '', 1)

# Write the updated content back to the same file
with open(file_path, 'w') as f:
    f.write(new_content)

print(f'The file "{filename}.json" has been updated!')
