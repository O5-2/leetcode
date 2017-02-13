# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        left = (root.left == None)
        right = (root.right == None)
        if left and right:
            if sum == root.val:
                return True
            else:
                return False
        elif left:
            return self.hasPathSum(root.right,sum-root.val)
        elif right:
            return self.hasPathSum(root.left,sum-root.val)
        else:
            return self.hasPathSum(root.right,sum-root.val) or self.hasPathSum(root.left,sum-root.val)
