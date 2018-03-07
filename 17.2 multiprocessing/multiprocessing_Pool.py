from multiprocessing import Pool
import time 

def f(x):
    return x*x

if __name__ == '__main__':
    start = time.clock()

    with Pool(5) as p:
        print(p.map(f, range(1000)))

    stop =  time.clock()
    print(stop-start)