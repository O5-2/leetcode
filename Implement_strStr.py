class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size = len(needle)
        for i in range(0,len(haystack)+1-len(needle)):
            if haystack[i:i+size] == needle:
                return i
        return -1
