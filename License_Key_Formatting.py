class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if set(S) == set("-"):
            return ""
        a = S.upper().split("-")
        b = "".join(a)
        n = sum([len(i) for i in a]) % K
        c = b[:n]+"-"
        d = b[n:]
        e = ""
        for i in range(0, len(b), K):
            e += d[i:i+K]+"-"
        if n != 0:
            e = c+e
        while e[-1] == "-":
            e = e[:-1]
        return e
