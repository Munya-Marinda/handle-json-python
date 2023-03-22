import requests
import json

file_names = [
"orders"
]

for filename in file_names:
    url = f'https://example.co.za/financial-report-api/api.php?{filename}=1&limit=7000000'
    file_path = f'{filename}.json'

    response = requests.get(url)

    if response.status_code == 200:
        with open(file_path, 'w') as f:
            f.write(response.text[:-4] + ']')
        
        print(f'Successfully downloaded and saved JSON data to "{file_path}".')
    else:
        print(f'Error downloading JSON data (HTTP status code {response.status_code}).') 
