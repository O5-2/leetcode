class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if (A == B) and (A == ""):
            return True
        if len(A) != len(B):
            return False
        for i in range(0, len(A)):
            if A == B:
                return True
            A = A[1:]+A[0]
        return False
