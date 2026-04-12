Numbers = [0, 1, 2, 3, 4, 5, 8, 9]

Number_Search = input("What number do you want from 0 - 9?")

Start = 0
End = 8

while Start <= End:
    Middle = (Start + End)//2
    print (Middle)
    print(Numbers[Middle])
    if Number_Search == Numbers[Middle]:
        print(str(Number_Search) + " is on my list.")
        break
    elif Number_Search != Numbers[Middle]:
        if Numbers[Middle] > Number_Search:
            End = Middle - 1
        elif Numbers[Middle] > Number_Search:
            Start = Middle + 1

if Start > End:
    print("Sorry, " + str(Number_Search) + " is not on my list")