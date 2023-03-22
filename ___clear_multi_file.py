file_names = [ 
    "orders", 
]

for file_name in file_names:
    with open(file_name + ".json", "w") as f:
        pass # we don't need to do anything, just open and immediately close the file to truncate it

