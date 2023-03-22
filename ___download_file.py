import requests
import json

# Prompt the user to enter a URL and a file name (without extension)
filename = input('Enter the name for the JSON file (without extension): ')
url = f'https://example.co.za/financial-report-api/api.php?{filename}=1'

# Hard-code the file format as ".json"
file_path = f'{filename}.json'

# Download the JSON data from the URL
response = requests.get(url)

# Save the JSON data to a file
if response.status_code == 200:
    with open(file_path, 'w') as f:
        f.write(response.text)
    print(f'Successfully downloaded and saved JSON data to "{file_path}".')
else:
    print(f'Error downloading JSON data (HTTP status code {response.status_code}).')

