class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        ans = 0
        s = list(s)
        s.sort()
        sInd = 0
        while True:
            if sInd == len(s):
                break
            if sInd+1 == len(s):
                break
            if s[sInd] == s[sInd+1]:
                sInd += 1
                ans += 2
            sInd += 1
        from collections import defaultdict
        dd = defaultdict(int)
        for i in s:
            dd[i] += 1
        for i in dd:
            if dd[i]%2 == 1:
                return ans+1
        return ans
