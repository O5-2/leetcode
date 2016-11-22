class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(3, len(bin(n))):
            if bin(n)[i] == "1":
                count += 1
        return count
