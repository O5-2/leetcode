class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target and nums[i+1] > target:
                return i+1
