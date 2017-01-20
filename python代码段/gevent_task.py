# #-*-coding = utf-8-*-
# #!/usr/bin/env python
# import gevent
# from gevent import Timeout
#
# seconds = 10
#
# timeout = Timeout(seconds)
# timeout.start()
#
# def wait():
#     gevent.sleep(10)
#
# try:
#     gevent.spawn(wait).join()
# except Timeout:
#     print('Could not complete')
