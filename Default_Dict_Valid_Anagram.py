class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        sdd = defaultdict(int)
        tdd = defaultdict(int)
        for i in s:
            sdd[i] += 1
        for i in t:
            tdd[i] += 1
        if sdd.keys() != tdd.keys():
            return False
        for i in sdd.keys():
            if sdd[i] != tdd[i]:
                return False
        return True
