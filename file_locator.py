# 5.23.21
# List Files by asking user for directory
import os,glob

fileLocation = str(input("Directory Location: "))
os.chdir(fileLocation)
for file in glob.glob("*.*"):
    print(file) # prints file name

    
