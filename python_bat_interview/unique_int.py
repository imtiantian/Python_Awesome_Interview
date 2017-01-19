问题7：在2.5亿个整数中找出不重复的整数，注，内存不足以容纳这2.5亿个整数。

首先我们考虑在内存充足的情况下，我们可以使用python中的字典结构。对2.5亿个数中的每一个数，出现一次，字典对应的值+1.
最后遍历字典，找出value为1的所有key。代码很简单，10行都不到。

内存不充足的话，我们可以有两种解决方案。
（1）：假设内存有（2.5*（10**8）*2）/8*(10**9) = 0.06G。那么我们可以使用bit数组，下面我详细解释一下上面内存的计算过程：
因为数据可能存在的方式只有三种：没出现过，出现了一次，出现了很多次。所以我们用2bit表示这三种状态。另外数据有2.5亿条，
总计需要内存2.5亿*2 bit，约等于0.6G。算法的过程大致如下：
"""
1:  初始化一个(2.5*10^8) * 2 bool数组，并且初始化为False，对于每一个整数，使用
    2个bit来表示它出现的次数： 0 0：出现0次 0 1：出现一次 1 1:出现多次
2:  遍历文件，当数据是第一次出现的时候，，更改属于它的两个bit状态：从 00变成01
3： 最后遍历文件找出bit为01的数字，那么这个数字只出现了一次
"""

from collections import defaultdict
import numpy as np
mark =np.zeros((2.5*(10**8),2),dtype=np.bool) #初始化一个(2.5*10^8) * 2 bool数组，并且初始化为False，对于每一个整数，使用
两个bit来表示它出现的次数： 0 0：出现0次 0 1：出现一次 1 1:出现多次
def get_unique_int():
    with open('bigdata') as file:       #bigdata:原始的2.5亿个整数大文件
        for num in file:
            if mark[num][0] == False and mark[num][1] == False:  #这个数第一次出现。那么更改属于它的2个bit
                mark[num][0] = True
                mark[num][1] = False
            else:
                mark[num][0] = True                              #出现了不止一次的数据，那么同意赋值 1 1
                mark[num][1] = True
    with open('bigdata') as file:       #bigdata:原始的2.5亿个整数大文件
        for num in file:
        if mark[num][0] == True and mark[num][1] == False:
            yield num
    
    
if __name__ == '__main__':
    unique_list = get_unique_int()   #返回一个不重复整数的迭代器
  
