# -*- coding:utf-8 -*-
#  重建二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def reConstructBinaryTree(self, pre, tin):
        d={}
        if len(pre)==0 or len(pre)==0:
            return
        for i in range(len(tin)):
            d[tin[i]]=i
        return self.preIn(pre,0,len(pre)-1,tin,0,len(tin)-1,d)

    def preIn(self,p,pi,pj,n,ni,nj,d):
        if pi>pj:
            return
        head=TreeNode(p[pi])
        index=d[p[pi]]
        head.left=self.preIn(p,pi+1,pi+index-ni,n,ni,index-1,d)
        head.right=self.preIn(p,pi+index-ni+1,pj,n,index+1,nj,d)
        return head
    def posTraverseTree(self,head):
        while head==None:
            return
        self.posTraverseTree(head.left)
        self.posTraverseTree(head.right)
        print head.val


pre=[5,3,2,1,4,8,7,6,10,9,11]
tin=[1,2,3,4,5,6,7,8,9,10,11]
s=Solution()
head=s.reConstructBinaryTree(pre,tin)
s.posTraverseTree(head)



