class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = Solution()
        if s == "":
            return 0
        if s[0] == "M":
            return 1000+sol.romanToInt(s[1:])
        if s[:2] == "CM":
            return 900+sol.romanToInt(s[2:])
        if s[0] == "D":
            return 500+sol.romanToInt(s[1:])
        if s[:2] == "CD":
            return 400+sol.romanToInt(s[2:])
        if s[0] == "C":
            return 100+sol.romanToInt(s[1:])
        if s[:2] == "XC":
            return 90+sol.romanToInt(s[2:])
        if s[0] == "L":
            return 50+sol.romanToInt(s[1:])
        if s[:2] == "XL":
            return 40+sol.romanToInt(s[2:])
        if s[0] == "X":
            return 10+sol.romanToInt(s[1:])
        if s[:2] == "IX":
            return 9+sol.romanToInt(s[2:])
        if s[0] == "V":
            return 5+sol.romanToInt(s[1:])
        if s[:2] == "IV":
            return 4+sol.romanToInt(s[2:])
        if s[0] == "I":
            return 1+sol.romanToInt(s[1:])
