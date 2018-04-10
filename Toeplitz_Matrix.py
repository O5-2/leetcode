class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        h = len(matrix)
        w = len(matrix[0])
        num = matrix[0][0]
        for i in range(0, min(h, w)):
            if num != matrix[i][i]:
                return False
        for i in range(1, h):
            num = matrix[i][0]
            for j in range(0, min(h-i, w)):
                if num != matrix[i+j][j]:
                    return False
        for i in range(1, w):
            num = matrix[0][i]
            for j in range(0, min(h, w-i)):
                if num !=  matrix[j][i+j]:
                    return False
        return True
