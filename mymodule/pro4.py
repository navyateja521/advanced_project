import multiprocessing

def cal_square(number,q):

    for i in number:
      q.put(i*i)

def add_num(number,q):
    for i in number:
     q.put(i+i)

if __name__=='__main__':
    num=[1,2,3,7,8]
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=cal_square,args=(num,q))
    p2=multiprocessing.Process(target=add_num,args=(num,q))
    print(p1.name)
    print(p2.name)
    p1.start()
    p1.join()
    p2.start()
    p2.join()

    while q.empty() is False:
         print(q.get())