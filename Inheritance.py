class Cat:
    def __init__(self, name, color, pattern, length, teeth, habitat):
        self.name = name
        self.color = color
        self.pattern = pattern
        self.length = length  
        self.teeth = teeth    
        self.habitat = habitat 
    def print(self):
        print("I am a" + self.name + ". My fur color is" + self.color + ". I have" + self.pattern + "coat. I am " + self.length + "long. My teeth are " + self.teeth + "long. I live in " + self.habitat + ".")

Tiger = Cat(" tiger", " orange", " a striped ", " 300 cm ", " 9 cm ", "a rainforest")
Tiger.print()