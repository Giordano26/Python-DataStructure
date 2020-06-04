fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From') : 
        email = line.split()
        if(len(email)) > 2:
            print (email[1])
            count = count + 1

print ("There were", count, "lines in the file with From as the first word")