Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30]

def Finding_Number(Numbers):
    Start = 0
    End = 29
    while Start <= End:
        Middle = (Start + End)//2
        if Middle == Numbers[Middle]:
            Start = Middle + 1
        elif Middle != Numbers[Middle]:
            End = Middle - 1
        
    if Start > End:
        Missing_Number = Start
        print(Missing_Number)

Finding_Number(Numbers)