def add(x):
    if x == 0:
        return
    #print(x)
    return(x % 10) + add(x // 10)

print(add(456))