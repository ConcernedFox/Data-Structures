Clone_Wars_Characters = ["Anakin", "Obi-Wan", "Ahsoka", "Rex"]

def Bubble(Clone_Wars_Characters):
    bubbles = 1
    while bubbles <= 6:
        for i in range(0,3,1):
            if len(Clone_Wars_Characters[i]) > len(Clone_Wars_Characters[i+1]):
                S_S = Clone_Wars_Characters[i+1]
                Clone_Wars_Characters[i+1] = Clone_Wars_Characters[i]
                Clone_Wars_Characters[i] = S_S
        bubbles +=1

Bubble(Clone_Wars_Characters)
print(Clone_Wars_Characters)