class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        if len(s) != len(t):
            return False
        s1 = [i for i in s]
        t1 = [i for i in t]
        s1.sort(key = None, reverse = False)
        t1.sort(key = None, reverse = False)
        return s1 == t1
