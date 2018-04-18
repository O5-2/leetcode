class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t = [i for i in T]
        new = ""
        for i in range(0, len(S)):
            while S[i] in t:
                t.remove(S[i])
                new += S[i]
        return new+("".join(t))
