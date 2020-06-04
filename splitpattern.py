text = 'From stephen.maquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = text.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])