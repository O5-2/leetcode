# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, cur_sum, pathSoFar, foundSoFar):
        """
        :type node: TreeNode
        :type cur_sum: int
        :type pathSoFar: List[int]
        :type foundSoFar: List[List[int]]
        :rtype: None? List[List[int]]?
        """
        left = node.left != None
        right = node.right != None
        if not left and not right:
            if cur_sum == node.val:
                foundSoFar.append(pathSoFar)
            return
        if left:
            self.helper(node.left, cur_sum-node.val, pathSoFar+[node.left.val], foundSoFar)
        if right:
            self.helper(node.right, cur_sum-node.val, pathSoFar+[node.right.val], foundSoFar)
    def pathSum(self, root, cur_sum):
        """
        :type root: TreeNode
        :type cur_sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        foundSoFar = []
        self.helper(root, cur_sum, [root.val], foundSoFar)
        return foundSoFar
