class Car:
    def __init__(self, color, brand, size, speed):
        self.color = color
        self.brand = brand
        self.size = size
        self.speed = speed
    def print(self):
        print("I am a car! My color is " + self.color + ". I am a " + self.brand + ". I am a " + self.size + ". My speed is " + str(self.speed))
    def set_Car(self):
        self.speed += 10
    def set_Car2(self):
        self.speed -= 10
Tesla = Car("white", "Tesla", "SUV", 0)
Tesla.set_Car()
Tesla.print()
Tesla.set_Car()
Tesla.print()
Tesla.set_Car()
Tesla.print()
Tesla.set_Car2()
Tesla.print()