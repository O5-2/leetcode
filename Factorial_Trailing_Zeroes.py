class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fives = 1
        zeroes = 0
        while n >= fives:
            fives *= 5
            zeroes += (n/fives)
        return zeroes
