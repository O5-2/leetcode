class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        index = 0
        for i in t:
            if i == s[index]:
                index += 1
            if index == len(s):
                break
        return index == len(s)
