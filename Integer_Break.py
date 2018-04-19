class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0, 0, 1, 2, 4, 6, 9]
        mult = [4, 3, 3]
        div = [3, 2, 2]
        prod = 9
        if n < len(ans):
            return ans[n]
        else:
            for i in range(6, n):
                prod = (prod*mult[i%3])/div[i%3]
        return int(prod)
