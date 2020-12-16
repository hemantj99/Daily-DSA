# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> List[int]:
        res = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                res.append(node.val)
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
        return res
