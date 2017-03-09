class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(g) == 0 or len(s) == 0:
            return 0
        g.sort()
        s.sort()
        gInd = 0
        sInd = 0
        ans = 0
        while True:
            if s[sInd] >= g[gInd]:
                ans += 1
                gInd += 1
                sInd += 1
            else:
                sInd += 1
            if gInd == len(g) or sInd == len(s):
                return ans
