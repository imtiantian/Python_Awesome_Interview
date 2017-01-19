# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        return self.check(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

    def check(self,T,t):
        if t==None:
            return True
        if T==None or T.val!=t.val:
            return False
        return self.check(T.left,t.left) and self.check(T.right,t.right)

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)
t1.left.right = TreeNode(5)
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(7)
t1.left.left.left = TreeNode(8)
t1.left.left.right = TreeNode(9)
t1.left.right.left = TreeNode(10)

t2 = TreeNode(2)
t2.left = TreeNode(4)
t2.left.left = TreeNode(8)
t2.right = TreeNode(5)
s=Solution()
print s.HasSubtree(t1,t2)
