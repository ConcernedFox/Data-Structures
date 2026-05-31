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

Quail = Queue(6)
print(Quail.size())
Quail.enqueue("Star Wars IV: A New Hope")
Quail.enqueue("Star Wars V: The Empire Strikes Back")
Quail.enqueue("Star Wars VI: Return of the Jedi")
Quail.display()
print(Quail.size())
Quail.enqueue("Star Wars I: The Phantom Menace")
Quail.enqueue("Star Wars II: Attack of the Clones")
Quail.enqueue("Star Wars III: Revenge of the Sith")
Quail.display()
print(Quail.size())
print(Quail.front())
print(Quail.dequeue())
print(Quail.front())
print(Quail.dequeue())
print(Quail.front())
print(Quail.dequeue())
print(Quail.front())
print(Quail.dequeue())
print(Quail.front())
print(Quail.dequeue())
print(Quail.front())
print(Quail.dequeue())
print(Quail.front())
print(Quail.dequeue())