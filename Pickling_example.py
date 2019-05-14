# --------------------------------#
# Title: Pickling Example"
# Dev: mseeley3
# Date: 5/13/19
# Changelog: (Who, When, What)
# mseeley3,5/13/19, Created Script
# find gihub repository here: https://github.com/mseeley3/IntroToProg-Python
# --------------------------------#

print("Please catagorize clothing colors.")

# Get inputs from the user
name = str(input("Enter an color: "))
temp = str(input("Enter if this color is cool or warm: "))
look = str(input("Enter if this color looks good or bad on you: "))
lstColor = [name, temp, look]
print(lstColor)

# store the data with the pickle.dump method
objFile = open("C:\\_PythonClass\\Color.dat", "ab")
import pickle
pickle.dump(lstColor, objFile)
objFile.close()

# read the data back with the same pickle.load method
objFile = open("C:\\_PythonClass\\Color.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()
print("Data has been saved via the pickling method.")

# creating text file to store data line by line
objFile = open("Color_check.txt", "a")
objFile.write(str(lstColor) + "\n")
objFile.close()
print("The data has also been saved as a normal text file.")