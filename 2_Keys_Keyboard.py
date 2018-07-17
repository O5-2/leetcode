class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        factors = []
        while n != 1:
            for i in range(2, n+1):
                if n%i == 0:
                    n = int(n/i)
                    factors.append(i)
                    break
        return sum(factors)
