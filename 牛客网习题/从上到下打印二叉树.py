# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        q = [root]
        r = []
        while q:
            node = q.pop(0)
            r.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return r