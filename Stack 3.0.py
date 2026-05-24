Stack = []

def Ancestors():
    STACK = int(input("Give me the amount of letter you want in your word"))
    passes = 1
    while passes <= STACK:
        input2 = input("Put a letter")
        Stack.append(input2)
        passes += 1
    print(Stack.pop() + Stack.pop() + Stack.pop() + Stack.pop() + Stack.pop() + Stack.pop())

Ancestors()