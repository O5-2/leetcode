class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        import collections
        odict1 = collections.OrderedDict({})
        set1 = set([])
        for i in range(0, len(s)):
            if s[i] in odict1:
                odict1.pop(s[i], None)
                set1.add(s[i])
            else:
                if s[i] not in set1:
                    odict1[s[i]] = i
        if odict1 == collections.OrderedDict({}):
            return -1
        keys = odict1.keys()
        first = keys[0]
        return odict1[first]
