List = [1,2,3,2,4,2]
def add(List):
    z = 0
    Input1 = int(input("Out of the four numbers, 1, 2, 3, and 4, which number do you want as your target?"))
    if len(List) == 0:
        return(0)
    for i in range(len(List)):
        if List[i] == Input1:
            z += 1
        
    print(z)

print(add(List))