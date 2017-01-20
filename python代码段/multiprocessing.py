#coding: utf-8
"""
多线程和map方法相结合
"""
import multiprocessing
import logging

def create_logger(i):
    print i

class CreateLogger(object):
    def __init__(self, func):
        self.func = func

if __name__ == '__main__':
    ilist = range(10)

    cl = CreateLogger(create_logger)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(cl.func, ilist)

    print "hello------------>"
#阻塞
    # coding: utf-8
    import multiprocessing
    import time


    def func(msg):
        print "msg:", msg
        time.sleep(3)
        print "end"


    if __name__ == "__main__":
        pool = multiprocessing.Pool(processes=3)
        for i in xrange(4):
            msg = "hello %d" % (i)
            pool.apply(func, (msg,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

        print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
        pool.close()
        pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
        print "Sub-process(es) done."
#非阻塞
#coding: utf-8
import multiprocessing
import time

def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in xrange(4):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print "Sub-process(es) done."
"""
两个程序在pool线程池使用的apply方法不同，结果不同，先执行close()是不让其他进程继续加入池中，然后在通过、
join()杀掉子进程
"""