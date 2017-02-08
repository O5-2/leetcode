# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left != None:
            left = self.minDepth(root.left)
        else:
            left = 0
        if root.right != None:
            right = self.minDepth(root.right)
        else:
            right = 0
        if left == 0:
            if right == 0:
                return 1
            else:
                return right+1
        elif right == 0:
            return left+1
        else:
            return min(left, right)+1
