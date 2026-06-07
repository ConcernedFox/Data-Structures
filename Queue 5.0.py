class Queue:
    def __init__(self):
        self.queue = ["A", "B", "C", "D", "E", "F", "G", "You"]

    def size(self):
        return(len(self.queue))

    def dequeue(self):
        if self.size() > 1:
            print(self.queue[0] + " got served!")
            self.queue.pop(0)

        elif self.size() == 1:
            input2 = input("You are in the front! Which ice cream flavor do you want\nChocolate\nVanilla\nStrawberry\nMint\nCotton Candy\nCookies n' Cream\nBlackcurrant\nWild n' Reckless\nRocky Road")
            print("Have a good day!")
        else:
            print("You have had your ice cream")

    def display(self):
        print(self.queue)

DD = Queue()
DD.display()
DD.dequeue()
DD.display()
DD.dequeue()
DD.display()
DD.dequeue()
DD.display()
DD.dequeue()
DD.display()
DD.dequeue()
DD.display()
DD.dequeue()
DD.display()
DD.dequeue()
DD.display()
DD.dequeue()