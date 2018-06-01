class Solution:
    def magicSquare(self, grid):
        for i in range(0, 2):
            for j in range(0, 2):
                if ((grid[i][j] < 1) or (grid[i][j] > 9)):
                    return False
        magic = grid[0][0]+grid[1][1]+grid[2][2]
        if (grid[2][0]+grid[1][1]+grid[0][2] != magic):
            return False
        for i in range(0, 2):
            if (grid[0][i]+grid[1][i]+grid[2][i] != magic):
                return False
        for i in range(0, 2):
            if (grid[i][0]+grid[i][1]+grid[i][2] != magic):
                return False
        if (sum([sum(i) for i in grid]) != 45):
            return False
        return True
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        squares = 0
        for i in range(0, len(grid)-2):
            for j in range(0, len(grid)-2):
                if Solution.magicSquare(self, [[grid[i][j],grid[i][j+1],grid[i][j+2]],[grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2]],[grid[i+2][j], grid[i+2][j+1],grid[i+2][j+2]]]):
                    squares += 1
        return squares
