#Find biggest of 3 numbers entered
a = int(input("Enter three numbers:"))
b = int(input())
c = int(input())
if a > b:
    if a > c:
        greater = a
    else:
        greater = c
elif b > c:
    greater = b
else:
    greater = c
print("Greater: ", +greater)
