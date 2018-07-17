class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif sum(nums[1:]) == 0:
            return 0
        left = 0
        right = sum(nums)-nums[0]
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
        return -1
