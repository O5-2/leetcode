class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        time = 0
        for i in range(0, len(timeSeries)):
            if i == len(timeSeries)-1:
                time += duration
            else:
                if timeSeries[i+1]-timeSeries[i] < duration:
                    time += timeSeries[i+1] - timeSeries[i]
                else:
                    time += duration
        return time
