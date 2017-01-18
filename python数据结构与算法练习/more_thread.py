# import urllib2
# import time
# from threading import Thread
#
#
# class GetUrlThread(Thread):
#     def __init__(self, url):
#         self.url = url
#         super(GetUrlThread, self).__init__()
#
#     def run(self):
#         resp = urllib2.urlopen(self.url)
#         print self.url, resp.getcode()
#
#
# def get_responses():
#     urls = [
#         'http://www.baidu.com',
#         'http://www.163.com',
#         'http://www.sina.com',
#         'http://www.qq.com',
#     ]
#     start = time.time()
#     threads = []
#     for url in urls:
#         t = GetUrlThread(url)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print "Elapsed time: %s" % (time.time() - start)
#
#
# get_responses()
# from threading import Thread
#
# # define a global variable
# some_var = 0
#
#
# class IncrementThread(Thread):
#     def run(self):
#         # we want to read a global variable
#         # and then increment it
#         global some_var
#         read_value = some_var
#         print "some_var in %s is %d" % (self.name, read_value)
#         some_var = read_value + 1
#         print "some_var in %s after increment is %d" % (self.name, some_var)
#
#
# def use_increment_thread():
#     threads = []
#     for i in range(50):
#         t = IncrementThread()
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print "After 50 modifications, some_var should have become 50"
#     print "After 50 modifications, some_var is %d" % (some_var,)
#
#
# use_increment_thread()
from threading import Thread
import time


class CreateListThread(Thread):
    def run(self):
        self.entries = []
        for i in range(10):
            time.sleep(0.1)
            self.entries.append(i)
        print self.entries


def use_create_list_thread():
    for i in range(3):
        t = CreateListThread()
        t.start()


use_create_list_thread()