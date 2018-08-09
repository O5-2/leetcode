class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        old1 = 1
        old2 = 2
        cur = -1
        for i in range(3, n+1):
            cur = old1+old2
            old1 = old2
            old2 = cur
        return cur
