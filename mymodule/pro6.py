import multiprocessing

def cal_square(number,res):

    for i,n in enumerate(number):
        res[i]=(n*n)

def add_num(number,res):
    for i,n in enumerate(number):
        res[i]=(n+n)

if __name__=='__main__':
    num=[1,2,3,7,8]
    res=multiprocessing.Array('i',5)
    # res1=multiprocessing.Array('i',5)
    p1=multiprocessing.Process(target=cal_square,args=(num,res))
    p2=multiprocessing.Process(target=add_num,args=(num,res))
    print(p1.name)
    print(p2.name)
    p1.start()
    p1.join()
    print(res[:])
    p2.start()
    p2.join()
    print(res[:])
    # print(res1[:])