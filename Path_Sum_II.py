# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ret = []
        left = (root.left != None)
        right = (root.right != None)
        if (not left) and (not right):
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        if left:
            temp = self.pathSum(root.left, sum-root.val)
            new_val = [[root.val] + i for i in temp]
            ret.extend(new_val)
        if right:
            temp = self.pathSum(root.right, sum-root.val)
            new_val = [[root.val] + i for i in temp]
            ret.extend(new_val)
        return ret
