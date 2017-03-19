class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = 2
        while x <= num:
            x *= 2
        return x-num-1
