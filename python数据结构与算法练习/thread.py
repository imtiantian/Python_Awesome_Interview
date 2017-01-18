# #!/usr/bin/python
# #-*-coding=utf-8-*-
# from threading import Thread
# import time
# def my_counter():
#     i =0
#     for _ in range(10000000):
#         i =i+1
#     return True
# #单线程执行
# def main():
#     thread_array={}
#     start_time=time.time()
#     for tid in range(2):
#         t= Thread(target=my_counter)
#         t.start()
#         t.join()
#     end_time=time.time()
#     print end_time-start_time
# #多线程执行
# def main():
#     thread_array={}
#     start_time=time.time()
#     for tid in range(2):
#         t= Thread(target=my_counter)
#         t.start()
#         thread_array[tid]=t
#     for i in range(2):
#         thread_array[i].join()
#     end_time=time.time()
#     print end_time-start_time
# if __name__ == '__main__':
#     main()
# #多线程比单线程慢1秒
import time
import urllib2
def get_responses():
    urls = [
        'http://www.baidu.com',
        'http://www.163.com',
        'http://www.sina.com',
        'http://www.qq.com',
    ]
    start = time.time()
    for url in urls:
        print url
        resp = urllib2.urlopen(url)
        print resp.getcode()
    print "time:%s"%(time.time()-start)
get_responses()
