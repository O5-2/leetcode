class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 0:
            return 0
        for i in range(0, len(arr)):
            if sorted(arr[:i+1]) == [i for i in range(0, i+1)]:
                z = [j-i-1 for j in arr[i+1:]]
                return 1+self.maxChunksToSorted(z)
