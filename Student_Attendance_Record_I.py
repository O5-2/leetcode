class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            if s == "AA":
                return False
            else:
                return True
        absent = 0
        if s[0] == "A":
            absent += 1
        if s[1] == "A":
            absent += 1
        for i in range(2, len(s)):
            if s[i] == "A":
                absent += 1
            if (s[i] == "L") and ((s[i-2] == s[i-1]) and (s[i-1] == s[i])):
                return False
        if absent <= 1:
            return True
        else:
            return False
