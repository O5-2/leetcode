class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        ans = 1
        if s[0] == " ":
            ans = 0
        waiting = False
        for i in range(0,len(s)):
            if s[i] == " ":
                waiting = True
            elif waiting == True:
                ans += 1
                waiting = False
        return ans
