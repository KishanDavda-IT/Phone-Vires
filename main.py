import os

# Set the target file size (in bytes)
target_size = 1024 * 1024 * 1024  # 1 GB

# Create the file with the target size
with open('huge_file.txt', 'wb') as f:
    # Write random bytes to the file until the target size is reached
    while f.tell() < target_size:
        f.write(os.urandom(1024))  # Write 1 KB of random bytes

print("File created successfully.")