from queue import Queue

que = Queue()

que.put(1)
que.put(2)
que.put(3)

print(que.get())
print(que.get())

print(que.qsize())
