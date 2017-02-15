# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, curLevel, curMaxes):
        """
        :type node: TreeNode
        :type curLevel: int
        :type curMaxes: List[int]
        :rtype: List[int]?
        """
        if curLevel < len(curMaxes):
            curMaxes[curLevel] = max(curMaxes[curLevel], node.val)
        else:
            curMaxes.append(node.val)
        if node.left != None:
            self.helper(node.left, curLevel+1, curMaxes)
        if node.right != None:
            self.helper(node.right, curLevel+1, curMaxes)
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        curMaxes = [root.val]
        self.helper(root, 0, curMaxes)
        return curMaxes
