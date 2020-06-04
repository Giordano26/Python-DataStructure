d = {'a':10, 'b':1,'c':22}
t = sorted(d.items())
print(t)
for k,v in sorted(d.items()): #loop in the dict through the value of the keys
    print(k,v) 
