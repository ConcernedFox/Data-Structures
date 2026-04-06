Cats = ["Cheetah", "Cougar", "Jaguar", "Leopard", "Lion", "Ocelot", "Serval", "Snow Leopard", "Tiger"]

That_One_Big_Cat = input("Name me a cat")

Start = 0
End = 8

while Start <= End:
    Middle = (Start + End)//2
    print (Middle)
    print(Cats[Middle])
    if That_One_Big_Cat == Cats[Middle]:
        print("This is in our list")
        break
    elif That_One_Big_Cat != Cats[Middle]:
        if Cats[Middle] > That_One_Big_Cat:
            End = Middle - 1
        elif Cats[Middle] < That_One_Big_Cat:
            Start = Middle + 1

if Start > End:
    print("This is not on my list")