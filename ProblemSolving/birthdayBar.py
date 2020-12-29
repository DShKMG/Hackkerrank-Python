def birthday(s, d, m):
    # S contain vector
    # d contains sum
    # m contain max subset length
    prevVal = 0
    for i in range(0, len(s)):
        if len(s[i:i+m]) == m:
            if (sum(s[i:i+m])) == d:
                prevVal += 1
    return prevVal


print(birthday([1, 2, 1, 3, 2], 3, 2))
