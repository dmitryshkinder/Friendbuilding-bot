import shutil
import sys

with open('./file.txt', encoding='utf-8') as file:
    array = [row.strip() for row in file]
    
print(array)