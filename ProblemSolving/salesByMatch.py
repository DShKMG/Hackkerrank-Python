a = [10, 20, 20, 10, 10, 30, 50, 10, 20]

mydict = dict()

for i in a:
    if i not in mydict:
        mydict[i] = 1
    else:
        mydict[i] += 1

print(mydict)
# Get floor division
print(list(mydict.values()))
totalpairs = 0
for i in list(mydict.values()):
    totalpairs += i//2

print(totalpairs)
