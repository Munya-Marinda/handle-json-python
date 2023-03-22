import json
import requests 

file_names = [
"orders",
]

for filename in file_names: 

    # Open the JSON file and load its contents
    with open(f"{filename}.json") as f:
        data = json.load(f)

    # Format the data as a JSON string with indentation and sorting
    formatted_data = json.dumps(data, indent=4)

    # Write the formatted data to a new file
    with open(f"{filename}.json", "w") as f:
        f.write(formatted_data)
