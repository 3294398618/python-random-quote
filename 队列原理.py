class Queue():
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self,data):
        self.queue.insert(0,data)
    
    def size(self):
        return len(self.queue)

    def dequeue(self):
        if len(self.queue):
            return self.queue.pop()
        return("队列是空的")

q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print("队列的长度是 :",q.size())
print("读取队列:",q.dequeue())
print("读取队列:",q.dequeue())
print("读取队列:",q.dequeue())
print("读取队列:",q.dequeue())