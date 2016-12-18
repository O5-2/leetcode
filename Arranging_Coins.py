class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int((math.sqrt(8*n + 1)-1)/2)
