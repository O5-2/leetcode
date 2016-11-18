class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return bool(0)
        if n == 1:
            return bool(1)
        for i in range(3, len(bin(n))):
            if bin(n)[i] != "0":
                return bool(0)
        return bool(1)
