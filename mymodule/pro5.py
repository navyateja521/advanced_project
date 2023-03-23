from concurrent.futures import ThreadPoolExecutor

import time
def study():
    for i in range(5):
        print("i am reading")
        time.sleep(2)


def sleeping():
    for i in range(5):
        print("i am sleeping")
        time.sleep(2)

if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(study)
        pool.submit(sleeping)

