class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        count = 2
        old = [1,1]
        new = []
        for i in range(0, rowIndex):
            new = []
            for j in range(0, count):
                if (j == 0) or (j == (count-1)):
                    new.append(1)
                else:
                    new.append(old[j-1]+old[j])
            old = new
            count += 1
        return new
