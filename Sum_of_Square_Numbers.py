class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        for i in range(0, int(sqrt(c))+1):
            if sqrt(c-(i*i)) % 1.0 == 0.0:
                return True
        return False
