class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times = []
        for i in timePoints:
            times.append(int(i[:2])*60 + int(i[3:]))
        times = sorted(times)
        cur = 1441
        for i in range(0, len(times)-1):
            cur = min(times[i+1]-times[i], cur)
        cur = min(cur, times[0]+1440-times[-1])
        return cur
