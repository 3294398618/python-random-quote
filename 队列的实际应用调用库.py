from queue import Queue


q = Queue
for i in range(3):
   q.put(i)
# empty 检测队列是否为空，空传回         真
while not q.empty():
    print(q.get())