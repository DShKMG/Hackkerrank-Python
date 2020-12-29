endP = 7
target = 4

amount = 0
turnPage = 0
startPbeg = 1
startPend = endP
for i in range(endP//2):
    if endP % 2 != 0:
        if (startPend-1) <= target:
            print(turnPage)
    if startPend <= target or startPbeg >= target:
        break
    else:
        turnPage += 1
        startPbeg += 2
        startPend -= 2

print(turnPage)
"""
for i in range(endP, startP, -2):
    if i <= target:
        break
    else:
        amount += 1

print(amount)

ramount = 0
for i in range(startP, endP, 2):
    if i >= target:
        break
    else:
        ramount += 1

print(ramount)
"""
