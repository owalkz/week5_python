try:
    with open("myfile.txt", "w") as File:
        File.write("Hello, this is a file handling assignment. Line 1.\n")
        File.write("This is the second line of the file. Line 2.\n")
        File.write("This is the third line of the file. Line 3\n")
except FileNotFoundError:
    print("File not found.")

try:
    with open("myfile.txt", "r") as File:
        print(File.read())
except FileNotFoundError:
    print("File not found.")

try:
    with open("myfile.txt", "a") as File:
        File.write("This is the fourth line of the file.\n")
        File.write("This is the fifth line of the file.\n")
        File.write("This is the sixth line of the file.\n")
except FileNotFoundError:
    print("File not found.")
