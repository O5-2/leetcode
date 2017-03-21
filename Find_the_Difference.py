class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) == 1:
            return t
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        s = ''.join(s)
        t = ''.join(t)
        for i in range(0,len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
