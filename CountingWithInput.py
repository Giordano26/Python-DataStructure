counts = dict()
print("Enter a line of text: ")
line = input('')
words = line.split()

print("Words: ", words)
print("Counting...")
for word in words:
    counts[word] = counts.get(word,0) + 1
for key,value in counts.items():
    print(key,value)