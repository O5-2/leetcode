class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        map = ["0", "1", "5", "10", "10", "2", "9", "10", "8", "6"]
        nums = 0
        for i in range(1, N+1):
            rot = ""
            broke = False
            for j in range(0, len(str(i))):
                k = str(i)[j]
                if k in ["3", "4", "7"]:
                    broke = True
                    break
                rot += map[int(k)]
            if (not broke) and (i != int(rot)):
                nums += 1
        return nums
