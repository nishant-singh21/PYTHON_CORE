# part2 of file handling 
# write operation

f  = open("demo.txt", "a")

f.write("Hello, world!")
f.write("\nThis is a new line.\n")
f.write("Appending data to the file.\n")
f.close()


# r+ = read and write mode(over write  from starting the file)
# w+ = write and read mode (overwrites the file)
# a+ = append and read mode (appends to the end of the file)(end of the file )
f = open("demo.txt", "a+")
f.write("abc\n")
f.close()

# with syantax
with open("demo.txt","a")as f:
    f.write("This is a new line added using the with syntax.\n")
    f.write("\n Appending a new line using the with syntax.\n ")


# delete operation
import os
os.remove("demo.txt")
