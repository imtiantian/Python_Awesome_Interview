from node import Node

class Solution(object):
    def ReverseList(self,pHead):
        node=pHead
        tmp=None
        while node!=None:
            next_node=node.next
            node.next=tmp
            tmp=node
            node=next_node
        return tmp

    def ReverseList_2(self,pHead):
        node=pHead
        node_list=[]
        while node!=None:
            node_list.append(node)
            node=node.next
        if len(node_list)==0:
            return None
        tmp=node_list.pop()
        head=tmp
        while len(node_list)!=0:
            node=node_list.pop()
            tmp.next=node
            tmp=node
        tmp.next=None
        return head



    def printReversedList(self,pHead):
        node=pHead
        while node!=None:
            print node.data
            node=node.next

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
s=Solution()
phead=s.ReverseList_2(head)
s.printReversedList(phead)