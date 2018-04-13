class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a = len(A)
        b = len(B)
        times = (b/a)+3
        for i in range(1, times):
            current = A*i
            for j in range(0, (a*i)-b+1):
                if current[j:j+b] == B:
                    return i
        return -1
