import multiprocessing
def cal():
    for i in range(10):
        print(i**3)
if __name__=='__main__':
    print(multiprocessing.cpu_count())
    p1=multiprocessing.Process(target=cal)
    print(p1.name)

    p1.start()
    print(p1.pid)