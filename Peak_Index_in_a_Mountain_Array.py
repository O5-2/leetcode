class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = max(A)
        for i in range(0, len(A)):
            if A[i] == m:
                return i
