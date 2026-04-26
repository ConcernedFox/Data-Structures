def exponent(a, n):
    if n == 0:
        return 1
    elif n != 0:
        return a*exponent(a, n-1)
    
print(exponent(27,2))