'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.ismirror(root,root)
    def ismirror(self,t1:TreeNode, t2:TreeNode):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        a=self.ismirror(t1.right, t2.left)
        b=self.ismirror(t1.left, t2.right)
        if t1.val==t2.val:
            if a==True and b==True:
                return True
        
