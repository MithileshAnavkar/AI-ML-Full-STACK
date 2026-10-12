import shutil
import os

source = input("Enter file path: ")
backup = source + ".backup"

if os.path.isfile(source):
    shutil.copy2(source, backup)
    print("Backup created:", backup)
else:
    print("File does not exist!")