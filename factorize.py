from multiprocessing import Process, cpu_count
from time import time


def factorize1(*number):
    final_list = []
    for n in number:
        list = []
        for i in filter(lambda x: n % x == False, range(1, n+1)):
            list.append(i)
        final_list.append(list)
    [print(el) for el in final_list]

def factorize2(n):
    list = []
    for i in range(1, n+1):
        if n % i == False:            
            list.append(i)
    print(list)


if __name__ == '__main__':

    timer = time()
    factorize1(128, 255, 99999, 10651060)
    print(time() - timer)

    timer = time()
    number = (128, 255, 99999, 10651060)
    for n in number:
        pr = Process(target=factorize2, args=(n, ))
        pr.start()
    print(time() - timer)
    
    print('Кількость ядер на машині: ', cpu_count())
