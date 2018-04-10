class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dom = max(nums)
        index = -1
        for i in range(0, len(nums)):
            if nums[i] == dom:
                index = i
        for i in range(0, len(nums)):
            if (nums[i]*2 > dom) and (i != index):
                return -1
        return index
