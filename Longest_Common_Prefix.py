class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = ""
        smallest = min([len(i) for i in strs])
        for i in range(0, smallest):
            common = True
            cur = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != cur:
                    common = False
            if common:
                prefix += strs[0][i]
            else:
                return prefix
        return prefix
