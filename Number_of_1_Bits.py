class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = bin(n)[2:]
        ans = 0
        for i in m:
            if i == "1":
                ans += 1
        return ans
