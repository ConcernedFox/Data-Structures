class Cat:
    def __init__(self, name, color, pattern, length,):
        self.name = name
        self.color = color
        self.pattern = pattern
        self.length = length 
    def print(self):
        print("I am a" + self.name + ". My fur color is" + self.color + ". I have" + self.pattern + "coat. I am " + self.length + "long.")

class Big_Cat(Cat):
    def __init__(self, name, color, pattern, length, teeth, habitat):
        Cat.__init__(self, name, color, pattern, length,)
        self.teeth = teeth    
        self.habitat = habitat 
    def print(self):
        print("I am a " + self.name + ". My fur color is " + self.color + ". I have " + self.pattern + "coat. I am " + self.length + "long. My teeth are " + self.teeth + "long. I live in a " + self.habitat + ".")

class House_Cat(Cat):
    def __init__(self, name, color, pattern, length, pet_name):
        Cat.__init__(self, name, color, pattern, length,)
        self.pet_name = pet_name
    def print(self):
        print("I am a" + self.name + ". My fur color is" + self.color + ". I have" + self.pattern + "coat. I am " + self.length + "long. My House name is " + self.pet_name + ".")

Tiger = Big_Cat("Tiger", "orange", "a striped ", "300 cm ", "10 cm ", "jungle")
Lion = Big_Cat("Lion", "golden", "a no patterned ", "295 cm ", "9.5 cm ", "savanna")
Jaguar = Big_Cat("Jaguar", "yellow", "a spotted ", "200 cm ", "8 cm ", "rainforest")
Leopard = Big_Cat("Leopard", "yellow", "a spotted ", "160 cm ", "5 cm ", "savanna")
Cougar = Big_Cat("Cougar", "grayinsh brown", "a no patterned ", "275 cm ", "5 cm", "mountains")
Tiger.print()
Lion.print()
Jaguar.print()
Cougar.print()
Leopard.print()