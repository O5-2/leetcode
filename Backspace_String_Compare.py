class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = ""
        for i in S:
            if i == "#":
                s = s[:-1]
            else:
                s += i
        t = ""
        for i in T:
            if i == "#":
                t = t[:-1]
            else:
                t += i
        return s == t
