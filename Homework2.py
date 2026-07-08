class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

class Dog(Animal):
    def __init__(self, name, sound):
        Animal.__init__(self,name, sound)
        
    def print(self):
        print("Hello, I am a " + self.name + self.sound)

class Cat(Animal):
    def __init__(self, name, sound):
        Animal.__init__(self,name, sound)
        
    def print(self):
        print("Hello, I am a " + self.name + self.sound)

Dog = Dog("Dog",". Woof, Woof!")
Cat = Cat("Cat", ". Meow, Meow!")
Dog.print()
Cat.print()