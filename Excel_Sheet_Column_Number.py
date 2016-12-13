class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        length = len(s)
        if length == 1:
            return ord(s) - 64
        else:
            for i in range(0, len(s)):
                num += (ord(s[i])-64) * (26**(len(s)-i-1))
            return num
