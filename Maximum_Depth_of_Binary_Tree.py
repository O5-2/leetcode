# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left != None:
            left = self.maxDepth(root.left)
        else:
            left = 0
        if root.right != None:
            right = self.maxDepth(root.right)
        else:
            right = 0
        return (max(left, right)+1)
