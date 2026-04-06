Mahabharath = ["Yudhisthir", "Bhim", "Arjun", "Nakul", "Sahadev", "Draupadi", "Kunti", "Krishna", "Duryodhan", "Dushashan", "Shakuni", "Karn", "Vikarn", "Bhishma", "Dron", "Ashwathama", "Abhimanyu", "Jayadrath", "Sanjay", "Kripacharya",]

Mahan = input("Name me a Mahabharath Character")

if Mahan in Mahabharath:
    print("Nice! You really know your stuff!")
elif Mahan not in Mahabharath:
    print("This might be a character, but isn't in my list")

found = False

for c in range(19):
    if Mahan == Mahabharath[c]:
        found = True
        print("Nice! You really know your stuff!")
        break
        
if found == False:
    print("This might be a character, but isn't in my list")