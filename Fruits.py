class Fruit:
    def __init__(self, name, color, taste, shape, preference):
        self.name = name
        self.color = color
        self.taste = taste
        self.__shape = shape#Hidden Variable
        self.preference = preference
    def print(self):
        print("Hello, I am " + self.name + "," + self.color + "," + self.taste + "," + self.__shape + "," + self.preference)
    def getname(self):
        return(self.name)    
    def set_Apple(self):
        self.color = "green"
        self.taste = "sour"
Apple = Fruit("Apple","red","sweet","round","I prefer this over banana")
Banana = Fruit("Banana","yellow","sweet","curved","I prefer this over pumpkin")
Apple.set_Apple()
Apple.print()
Banana.print()
print(Apple.getname())
print(Banana.getname())
#print(Apple.__shape)