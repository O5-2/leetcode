class Solution(object):
    def helper(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        spiral = []
        twoColumns = False
        if len(matrix) == 1:
            return matrix[0]
        elif len(matrix[0]) == 1:
            for i in range(0,len(matrix)):
                spiral.append(matrix[i][0])
            return spiral
        elif len(matrix[0]) == 2:
            twoColumns = True
        for i in range(0, len(matrix[0])):
            spiral.append(matrix[0][i])
        for i in range(1, len(matrix)):
            spiral.append(matrix[i][-1])
        for i in range(2, len(matrix[-1])+1):
            spiral.append(matrix[-1][i*-1])
        for i in range(2, len(matrix)):
            spiral.append(matrix[i*-1][0])
        for i in range(0, len(matrix)):
            matrix[i] = matrix[i][1:-1]
        if not twoColumns:
            spiral.extend(self.helper(matrix[1:-1]))
        return spiral
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = self.helper(matrix)
        return spiral
