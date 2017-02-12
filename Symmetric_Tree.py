# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isMirror(self, rootA, rootB):
        """
        :type rootA: TreeNode
        :type rootB: TreeNode
        :rtype: bool
        """
        if (rootA == None) or (rootB == None):
            if rootA == rootB:
                return True
            else:
                return False
        else:
            return (self.isMirror(rootA.left, rootB.right) and self.isMirror(rootA.right, rootB.left)) and (rootA.val == rootB.val)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
