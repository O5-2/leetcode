class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(0, 20):
            strN = str(n)
            n = 0
            for j in range(0, len(strN)):
                n += int(strN[j])**2
        if n == 1:
            return bool(1)
        else:
            return bool(0)
