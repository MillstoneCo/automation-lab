#look in this folder
#count files in folder
#store count in variable
#print variable


import os

count = 0

for item in os.listdir("./test-data"):
    count = count + 1
print(f"There are {count} files in this folder.")

