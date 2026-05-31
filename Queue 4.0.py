class Queue:
    def __init__(self, n):
        self.queue = []
        self.n = n

    def size(self):
        return(len(self.queue))

    def enqueue(self, m):
        if self.size() < self.n:
            self.queue.append(m)
        else:
            print("QUEUE IS FULL!!!")

    def display(self):
        print(self.queue)

    def dequeue(self):
        if self.size() >= 1:
            return(self.queue.pop(0))
        else:
            print("NO ELEMENT LEFT TO DELETE!!!")

    def front(self):
        if self.size() >= 1:
            return(self.queue[0])
        else:
            print("NO FRONT ELEMENT TO PRINT!!!")

Quail = Queue(3)
print(Quail.size())
Quail.enqueue("Doc 1")
Quail.enqueue("Doc 2")
Quail.enqueue("Doc 3")
Quail.display()
print("Printing " + Quail.dequeue() + ".")
print("Printing " + Quail.dequeue() + ".")
print("Printing " + Quail.dequeue() + ".")