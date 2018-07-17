class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ints = sorted(nums)
        mins = 0
        for i in range(0, len(ints), 2):
            mins += ints[i]
        return mins
