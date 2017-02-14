# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, pathSoFar, foundSoFar):
        """
        :type root: TreeNode
        :type pathSoFar: string
        :type foundSoFar: List[str]
        :rtype: List[str]
        """
        if (root.left == None) and (root.right == None):
            foundSoFar.append(pathSoFar)
            return
        if root.left != None:
            self.helper(root.left, "->".join([pathSoFar, str(root.left.val)]), foundSoFar)
        if root.right != None:
            self.helper(root.right, "->".join([pathSoFar, str(root.right.val)]), foundSoFar)
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        found = []
        self.helper(root, str(root.val), found)
        return found
