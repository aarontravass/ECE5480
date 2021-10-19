import os
 
# INPUT THE BASE DIRECTORY
base_directory = input("Enter a directory = ")

# USE os.listdir() to create a list of all the files and directories in the base directory
directory_contents = os.listdir(base_directory)

# create an empty files list and an empty dirs list
files = []
dirs = []

for item in directory_contents:
    path=os.path.join(base_directory,item)
    if(os.path.isfile(path)):
        files.append(path)
    elif(os.path.isdir(path)):
        dirs.append((path))

if(len(files)==0):
    print("No files found")
else:
    outfile = open("files.txt", "a")
    print("Following are the files found")
    for file in files:
        print(file)
        outfile.write(file+"\n")
    print("\n")
    outfile.close()

if(len(dirs)==0):
    print("No directories found")
else:
    outfile = open("directors.txt", "a")
    print("Following are the directories found")
    for dir in dirs:
        print(dir)
        outfile.write(dir+"\n")
    # write your found files to a text file
    outfile.close()
# write your found directories to a text file

  