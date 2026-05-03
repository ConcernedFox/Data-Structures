Star_Wars_Movies = ["Episode 4: A New Hope", "Episode 2: Attack of the Clones", "Episode 6: Return of the Jedi", "Episode 3: Revenge of the Sith", "Episode 5: The Empire Strikes Back", "Episode 1: The Phantom Menace"]

def passing(Star_Wars_Movies):
    passes = 1
    while passes <= 6:
        for i in range(0, 5, 1):
            if Star_Wars_Movies[i] < Star_Wars_Movies[i+1]:
                S_S = Star_Wars_Movies[i+1]
                Star_Wars_Movies[i+1] = Star_Wars_Movies[i]
                Star_Wars_Movies[i] = S_S
        passes += 1

passing(Star_Wars_Movies)
print(Star_Wars_Movies)