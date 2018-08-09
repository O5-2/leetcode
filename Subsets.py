class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums, []]
        else:
            s = self.subsets(nums[:-1])
            return [i+[nums[-1]] for i in s]+s
