class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        count = 2
        triangle = [[1]]
        for i in range(1, numRows):
            current = []
            for j in range(0, count):
                if (j == 0) or (j == (count-1)):
                    current.append(1)
                else:
                    current.append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle.append(current)
            count += 1
        return triangle
