# Ask for the filename
filename = input("Enter the JSON filename (excluding extension): ")

# Read the contents of the JSON file into a string
with open(f"{filename}.json", "r") as f:
    json_text = f.read()

# Calculate the size of each chunk
chunk_size = len(json_text) // 15

# Split the text into chunks of roughly equal size
chunks = [json_text[i:i+chunk_size] for i in range(0, len(json_text), chunk_size)]

# If there are any remaining characters, add them to the last chunk
if len(chunks) > 15:
    last_chunk = chunks.pop()
    chunks[-1] += last_chunk

# Write each chunk to a separate file
for i, chunk in enumerate(chunks):
    with open(f"{filename}-p{i+1}.json", "w") as f:
        f.write(chunk)

