class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strings = s.split(" ")
        newStrings = []
        for i in strings:
            if i != "":
                newStrings.append(i)
        if newStrings == []:
            return 0
        return len(newStrings[-1])
