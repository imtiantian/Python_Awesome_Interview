# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        re = []
        if listNode is None:
            return re
        while listNode.next is not None:
            re.append(listNode.val)
            listNode = listNode.next

        re.append(listNode.val)
        return re[::-1]


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here

        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l
    # 输入一个链表，从尾到头打印链表每个节点的值。