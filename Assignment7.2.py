fname = input('Enter file name: ')
fh = open(fname)
count = 0
macaco = 0.0
for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    cuc = line.find('0')
    number = line[cuc:]
    numberF = float(number)
    macaco = macaco + numberF

zelda = macaco / float(count)
print('Average spam confidence:',zelda)


