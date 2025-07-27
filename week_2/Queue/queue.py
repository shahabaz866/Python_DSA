class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def display(self):
        if not self.is_empty():
            print("Queue elements:")
            for item in self.queue:
                print(item)
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
q.display()
print("Dequeued:", q.dequeue())
q.display()
