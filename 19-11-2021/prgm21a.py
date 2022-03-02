#A-Generate positive list of numbers from a given list of integer
list = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]
nlist = [i for i in list if i > 0]
print(nlist)