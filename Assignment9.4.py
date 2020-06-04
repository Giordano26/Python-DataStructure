name = input("Enter file:")
handle = open(name)

lst = list()

for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for email in lst:
    counts[email] = counts.get(email,0) + 1

bigSender = None
times = None
for key,value in counts.items(): 
    if bigSender is None or value > bigSender:
        bigSender = value
        times = key

print (times,bigSender)
