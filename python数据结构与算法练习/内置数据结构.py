#-*-coding=utf-8-*-
# def test1():
#    l = []
#    for i in range(1000):
#       l = l + [i]
# def test2():
#    l = []
#    for i in range(1000):
#       l.append(i)
# def test3():
#    l = [i for i in range(1000)]
# def test4():
#    l = list(range(1000))
#
#
# from timeit import Timer
#
# t1 = Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000), "milliseconds")
# t2 = Timer("test2()", "from __main__ import test2")
# print("append ",t2.timeit(number=1000), "milliseconds")
# t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000), "milliseconds")
# t4 = Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000), "milliseconds")
# #构建栈，解决逆波兰表达式，求一个十进制数的二进制表达，检查括号匹配问题以及图的深度搜索等等
# class Stack:
#     def __init__(self):
#         self.items=[]
#     def is_empty(self):
#         return self.items==[]
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         return self.items[len(self.items)-1]
#     def size(self):
#         return len(self.items)
# #构建队列，解决优先队列和广度搜索
# class Queue:
#     def __init__(self):
#         self.items=[]
#     def is_empty(self):
#         return self.items==[]
#     def enqueue(self,item):
#         self.items.insert(0,item)
#     def dequeue(self):
#         return self.items.pop()
#     def size(self):
#         return len(self.items)
#     #双向队列，两端都可以插入和删除
#     #右端为front，左端为rear
#     class Deque:
#         def __init__(self):
#             self.items = []
#
#         def is_empty(self):
#             return self.items == []
#
#         def add_front(self, item):
#             self.items.append(item)
#
#         def add_rear(self, item):
#             self.items.insert(0, item)
#
#         def remove_front(self):
#             return self.items.pop()
#
#         def remove_rear(self):
#             return self.items.pop(0)
#
#         def size(self):
#             return len(self.items)
#实现二叉树（list方法），可读性差
# def binary_tree(r):
#     return [r, [], []]
# def insert_left(root, new_branch):
#     t = root.pop(1)
#     if len(t) > 1:
#         #new_branch becomes the left node of root, and original left
#         #node t becomes left node of new_branch, right node is none
#         root.insert(1, [new_branch, t, []])
#     else:
#         root.insert(1, [new_branch, [], []])
#     return root
# def insert_right(root, new_branch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2, [new_branch, [], t])
#     else:
#         root.insert(2, [new_branch, [], []])
#     return root
# def get_root_val(root):
#     return root[0]
# def set_root_val(root, new_val):
#     root[0] = new_val
# def get_left_child(root):
#     return root[1]
# def get_right_child(root):
#     return root[2]
#
# r = binary_tree(3)
# # insert_left(r, 4)
# #
# # insert_left(r, 5)
#
# # insert_right(r, 6)
# # insert_right(r, 7)
# # print(r)
# # l = get_left_child(r)
# # print(l)
# print set_root_val(r,9)
# # print(r)
# # insert_left(l, 11)
# # print(r)
# # print(get_right_child(get_right_child(r)))
# print r
class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None
    def insert_left(self,new_node):
        if self.left_child==None:
            self.left_child=BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key
#二叉堆：根据堆的性质又可以分为最小堆和最大堆，是一种非常好的优先队列。
        # 在最小堆中孩子节点一定大于等于其父亲节点，最大堆反之。
        # 二叉堆实际上一棵完全二叉树，
        # 并且满足堆的性质。对于插入和查找操作的时间复杂度度都是$O(logn)$。
class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    def perc_up(self, i):
        while i // 2 > 0: # >0 means this node is still available
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)
    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc
    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:] #append original list
        while (i > 0):
            #build the heap we only need to deal the first part!
            self.perc_down(i)
            i=i-1

a_list=[9, 6, 5, 2, 3]
bh=BinHeap()
bh.build_heap(a_list)
print(bh.heap_list)
print(bh.current_size)
# bh.insert(10)
# bh.insert(7)
# print(bh.heap_list)
# bh.del_min();
# print(bh.heap_list)
# print(bh.current_size)