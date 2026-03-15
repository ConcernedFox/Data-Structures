def printing(n):
    if n == 101:
        return
    print(n)
    printing(n + 1)

printing(1)