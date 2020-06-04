c = {'a':10, 'b':1, 'c': 22}
tmp = list()
for k , v in c.items(): #transform into list
    tmp.append((v,k)) 
print(tmp) # create a new touple but switches the values between v and k
tmp = sorted(tmp,reverse = True) #sort high to low "reverse = True"
print(tmp)
