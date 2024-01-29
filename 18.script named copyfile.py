#18. Write a script named copyfile.py. This script should prompt the user for the names of two text files. The contents of the first file should be input and written to the second file .

#Note: create a text file as “input.txt” and write some date in it. This will be used in the program.
with open("input.txt") as input:
    with open("output.txt","w") as output:
        for line in input: output.write(line)
print("JOB DONE!!")
