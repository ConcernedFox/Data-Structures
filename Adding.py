def add(x):
    if x == 0:
        return 0
    #print(x)
    return(x % 10) + add(x // 10)

print(add(456))