# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    global foundSoFar
    def helper(self, node, pathSoFar):
        """
        :type node: TreeNode
        :type pathSoFar: int
        :rtype: None
        """
        global foundSoFar
        left = node.left != None
        right = node.right != None
        if not left and not right:
            foundSoFar += pathSoFar
            return
        if left:
            self.helper(node.left, (pathSoFar*10)+node.left.val)
        if right:
            self.helper(node.right, (pathSoFar*10)+node.right.val)
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global foundSoFar
        if root == None:
            return 0
        foundSoFar = 0
        self.helper(root, root.val)
        return foundSoFar
