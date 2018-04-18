class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(1, len(s)+1):
            for j in range(0, len(s)-i+1):
                if s[j:j+i] == s[j:j+i][::-1]:
                    count += 1
        return count
