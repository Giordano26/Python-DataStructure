fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split
    for word in words:
        count[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
lst = sorted(lst, reverse = True)
for val, key in lst[:10]: #lst[:10] the highest 10 most common words
    print(key,val)
