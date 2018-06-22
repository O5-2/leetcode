class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        longestRow = 0
        current = 0
        i = 0
        while i < len(seats):
            if seats[i] == 0:
                current += 1
            else:
                longestRow = max(longestRow, current)
                current = 0
            i += 1
        longestRow = max(longestRow, current)
        if (seats[:longestRow] == [0]*longestRow) or (seats[-1*longestRow:] == [0]*longestRow):
            return longestRow
        edge1 = 0
        while seats[edge1] == 0:
            edge1 += 1
        edge2 = 0
        while seats[-1*(edge2+1)] == 0:
            edge2 += 1
        return max(int((longestRow+1)/2), max(edge1, edge2))
