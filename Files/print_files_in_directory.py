import glob
import os


os.chdir("D:\Development\Python\Files")
for file in glob.glob("*.py"):
    print(file)

