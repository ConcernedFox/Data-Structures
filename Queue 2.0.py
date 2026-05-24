class Queue:
    def __init__(self, n):
        self.queue = []
        self.n = n
    
    def adding():
        input1 = input("What is you favorite ice cream?")
        self.queue.append(input1)

    def remove():
        input2 = input("How many values do you want to remove")
        queue = len(self.queue)
        if queue <= input2:
            self.queue.remove(0)

Stare = Queue
Stare.adding()
Stare.remove()