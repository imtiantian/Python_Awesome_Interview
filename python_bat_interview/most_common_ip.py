

海量日志数据，提取出某日访问百度次数最多的那个IP


"""问题一：海量日志数据，提取出某日访问百度次数最多的那个IP
   解决思路：因为问题中提到了是海量数据，所以我们想把所有的日志数据读入内存，再去排序，找到出现次数最多的，显然行不通了。这里
   我们假设内存足够，我们可以仅仅只用几行代码，就可以求出最终的结果"""：
   代码如下：
   #python2.7
   from collections import Counter
   if __name__ == '__main__':
      ip_list = read_log()     #读取日志到列表中，这里为了简化，我们用一个小的列表来代替。
      ip_list = ["192.168.1.2"，"192.168.1.3","192.168.1.3","192.168.1.4","192.168.1.2"]
      ip_counter = Counter(ip_list) #使用python内置的计数函数，进行统计
      #print ip_counter.most_common() Out:[('192.168.1.3', 2), ('192.168.1.2', 2), ('192.168.1.4', 1)]
      print ip_counter.most_common()[0][0]    #out:192.168.1.3
   在内存足够的情况下，我们可以看到仅仅使用了5、6行代码就解决了这个问题
   """
   下面才是我们的重点，加入内存有限，不足以装得下所有的日志数据，应该怎么办？
   既然内存都不能装得下所有数据，那么我们后面的使用排序算法都将无从谈起，这里我们采取大而化小的做法。
   假设海量的数据的大小是100G，我们的可用内存是1G.我们可以把数据分成1000份（这里只要大于100都是可以的），每次内存读入100M
   再去处理。但是问题的关键是怎么将这100G数据分成1000分呢。这里我们以前学过的hash函数就派上用场了。
   Hash函数的定义：对于输入的字符串，返回一个固定长度的整数，hash函数的巧妙之处在于对于相同的字符串，那么经过hash计算，
   得出来的结果肯定是相同的，不同的值，经过hash，结果可能相同（这种可能性一般都很小）或者不同。那么有了hash函数，
   那么这道题就豁然开朗了，思路如下：
   1.对于海量数据中的每一个ip，使用hash函数计算hash(ip)%1000,输出到1000个文件中
   2.对于这1000个文件，分别找出出现最多的ip。这里就可以用上面提到的Counter类的most_common()方法了（这里方法很多，不一一列举）
   3.使用外部排序，对找出来的1000个ip在进行排序。（这里数据量小，神马排序方法都行，影响不大）
   代码如下：可以直接运行
   
import os
import heapq
import operator
from collections import Counter
source_file = 'C:/Users/Administrator/Desktop/most_ip/bigdata.txt'  #原始的海量数据ip
temp_files = 'C:/Users/Administrator/Desktop/most_ip/temp/'         #把经过hash映射过后的数据存到相应的文件中
top_1000ip = []                                                     #存放1000个文件的出现频率最高的ip和出现的次数
def hash_file():
    """
     this function is map a query to a new file
    """
    temp_path_list = []
    if not os.path.exists(temp_files):
        os.makedirs(temp_files)
    for i in range(0,1000):
        temp_path_list.append(open(temp_files+str(i)+'.txt',mode='w'))
    with open(source_file) as f:
        for line in f:
            temp_path_list[hash(str(line))%1000].write(line)
            #print hash(line)%1000
            print line
    for i in range(1000):
        temp_path_list[i].close()
def cal_query_frequency():
    for root,dirs,files in os.walk(temp_files):
        for file in files:
            real_path = os.path.join(root,file)
            ip_list = []
            with open(real_path) as f:
                for line in f:
                    ip_list.append(line.replace('\n',''))
            try:
                top_1000ip.append(Counter(ip_list).most_common()[0])
            except:
                pass
    print top_1000ip
def get_ip():
    return (sorted(top_1000ip,key = lambda a:a[1],reverse=True)[0])[0]
if __name__ == '__main__':
   hash_file()
   cal_query_frequency()
   print(get_ip())



