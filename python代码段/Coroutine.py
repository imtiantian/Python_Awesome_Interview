#-*-coding=utf-8-*-
#python的yield实现协程
# def foo():
#     print "foo start"
#     r=""
#     while True:
#         num = yield r
#         print num
#         r = "ok"
# if __name__=="__main__":
#     f =foo()
#     f.next()
#     print "begin start"
#     for x in range(5):
#         r =f.send(x)
#         print r
#     f.close()

"""
gevent库实现
"""
import gevent,random
def task(num):
    gevent.sleep(random.randint(0,2)*0.01)
    print "task %d is done"%num
def synchronous():
    for i in xrange(10):
        task(i)
def asychronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)
if __name__=="__main__":
    synchronous()
    print "="*20
    asychronous()