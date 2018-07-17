class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        newK = ""
        for i in range(0, len(s), 2*k):
            newK += s[i:i+k][::-1]
            newK += s[i+k:i+k+k]
        return newK
