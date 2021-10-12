import os
 
# INPUT THE BASE DIRECTORY
base_directory = input("Enter a directory = ")

# USE os.listdir() to create a list of all the files and directories in the base directory
directory_contents = os.listdir(base_directory)

# create an empty files list and an empty dirs list
files = []
dirs = []

for item in directory_contents:
    if(os.path.isfile(item)):
        files.append(item)
    elif(os.path.isdir(item)):
        dirs.append((item))


outfile = open("files.txt", "a")
print("Following are the files found")
for file in files:
    print(base_directory+"\\"+file)
    outfile.write(base_directory+"\\"+file+"\n")
print("\n")
outfile.close()
outfile = open("directors.txt", "a")

print("Following are the directories found")
for dir in dirs:
    print(base_directory+"\\"+dir)
    outfile.write(base_directory + "\\" + dir+"\n")
# write your found files to a text file
outfile.close()
# write your found directories to a text file

  