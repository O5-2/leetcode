class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        dom = -1
        for i in range(1, len(nums)):
            cur = 1
            j = i
            for j in range(i, len(nums)):
                if nums[j] > nums[j-1]:
                    cur += 1
                else:
                    break
            dom = max([cur, dom])
        return dom
