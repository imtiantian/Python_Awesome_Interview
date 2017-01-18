# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        #由图可得出，左右子树互换
        if not root:
            return None
        tmp = root.left
        root.left = self.Mirror(root.right)
        root.right = self.Mirror(tmp)
        return root