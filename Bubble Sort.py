Star_Wars_Movies = ["Episode 4: A New Hope", "Episode 2: Attack of the Clones", "Episode 6: Return of the Jedi", "Episode 3: Revenge of the Sith", "Episode 5: The Empire Strikes Back", "Episode 1: The Phantom Menace"]

def passes(Star_Wars_Movies):
    passing = 1
    while passing <= 6:
        for i in range(0, 5, 1):
            if Star_Wars_Movies[i] > Star_Wars_Movies[i+1]