Stack = []

def Push_And_Pop():
    global Stack
    input1 = int(input("Give an amount of values to add"))
    passes = 1
    while passes <= input1:
        input2 = input("Give me a value to add")
        Stack.append(input2)
        passes += 1

def Pop_And_Push():
    global Stack
    print(Stack)
    passes = 1
    input3 = int(input("Here is the stack. How many do you want to remove?"))
    while passes <= input3:
        Stack.pop()

Push_And_Pop()
print(Stack)
Pop_And_Push()