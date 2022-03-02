#Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.
n = 'alan'
c = n[0]
for i in n:
    if i==c:
     n= n.replace(i,'$')
     n=c+n[1:]
print(n)