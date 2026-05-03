Star_Wars_Movies = ["10: Lucknow Super Giants", "01: Punjab Kings", "07: Dehli Capitals", "04: Rajasthan Royals", "05: Gujarat Titans", "08: Kolkata Night Riders", "03: Sunrisers Hyderbad", "09: Mumbai Indians", "02: Royal Challengars Bangaluru", "06: Chennai Super Kings"]

def Insertion(Star_Wars_Movies):
    for i in range(1,10,1):
        A = Star_Wars_Movies[i]
        B = i-1
        while B >= 0 and A < Star_Wars_Movies[B]:
            Star_Wars_Movies[B+1] = Star_Wars_Movies[B]
            B = B-1
        Star_Wars_Movies[B+1] = A

Insertion(Star_Wars_Movies)
print(Star_Wars_Movies)