class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transposed = []
        for i in range(0, len(A[0])):
            current = []
            for j in range(0, len(A)):
                current.append(A[j][i])
            transposed.append(current)
        return transposed
