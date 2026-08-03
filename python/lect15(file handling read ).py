#  file handling read i/o operation
#  r= read , t = text 
f = open("text.txt", "r")
# data = f.read()
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close()

# mode 
# 'r' - Read (default)
# 'w' - Write (creates a new file or truncates an existing file)
# 'x' - Create (creates a new file, fails if the file already exists)
# 'a' - Append (adds data to the end of the file)
# 't' - Text (default)
# '+' - Update (read and write)