a = [1, 1, 1, 2, 2, 2, 1, 3, 2, 2, 2, 1, 2, 3]
mydict = {}

for i in a:
    if i not in mydict:
        mydict[i] = 0
    mydict[i] = mydict[i]+1

print(mydict)
print(len(mydict.values()))  # Total different items
for j in mydict.items():
    print(j[1])  # 1 for the values 0 for the keys
bString = "This is a string"
print(bString[::-1])
# Push back into a array of chars
arrChar = ['t', 'h', 'i', 's']
for i in range(len(arrChar)-1, 0, -1):
    print(arrChar[i])
