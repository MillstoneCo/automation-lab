


import os

for item in os.listdir("./test-data"):
    file_info = os.stat("./test-data/" + item)
    file_size = file_info.st_size
    print(f"{item} - {file_size / 1048576:.2f} MB")
