import time
from threading import Thread
from queue import Queue

class Producer():
    def __init__(self):
        self.q=Queue()
    def producer(self):
        for i in range(1,6):
            print('item producer' ,i)
            self.q.put(i)
            time.sleep(1)
class Customer():
    def __init__(self,prod):
        self.prod= prod
    def customer(self):
        for i in range(1,6):
            print("item received",self.prod.q.get(i))
p=Producer()
c=Customer(p)


t1=Thread (target=p.producer)
t2=Thread(target=c.customer)

t1.start()
t2.start()