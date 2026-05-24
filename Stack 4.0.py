class Stack:
    def __init__(self, n):
        self.stack = []
        self.n = n
    
    def size(self):
        return(len(self.stack))
    
    def push(self, m):
        if self.size() < self.n:
            self.stack.append(m)
        else:
            print("Stack is full. Can not add " + str(m) + ".")

    def display(self):
        print(self.stack)

    def pop(self):
        stack = 1
        if stack <= self.size():
            print(self.stack.pop(),end='')
        else:
            print("Sorry, can't pop anymore.")

input = input("Enter a word")
Star = int(len(input))
print(len(input))
Stare = Stack(len(input))
for i in input:
    Stare.push(i)
Stare.display()
for i in range(Star):
    Stare.pop()