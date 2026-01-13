import os

# Specify the directory path ('.' for current directory)
path = "/new folder"

# Get all files and folders
entries = os.listdir(path)

print(f"Contents of '{path}':")
for entry in entries:
    print(entry)