class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = len(nums)
        return ((x*x)+x)/2 - sum(nums)
