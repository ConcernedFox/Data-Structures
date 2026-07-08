Cats = ["Cheetah", "Cougar", "Jaguar", "Leopard", "Lion", "Ocelot", "Serval", "Snow Leopard", "Tiger"]
#Linear Search
That_One_Big_Cat = input("Name me a cat")

if That_One_Big_Cat in Cats:
    print("Nice! You know your stuff when it comes to Cats!")
elif That_One_Big_Cat not in Cats:
    print("Sorry, this is not on my list.")

found = False

for c in range(8):
    if That_One_Big_Cat == Cats[c]:
        found = True
        print("Nice! You know your stuff when it comes to Cats!")
        break

if found == False:
    print("Sorry, this cat is not on my list.")