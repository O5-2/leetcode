class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        found = False
        for i in range(0,len(nums)):
            if nums[i] == val:
                found = True
                low = i
                break
        if not found:
            return len(nums)
        high = 0
        highSet = False
        for i in range(low,len(nums)):
            if nums[i] != val:
                high = i
                highSet = True
                break
        if not highSet:
            high = len(nums)
        nums[low:] = nums[high:]
        return len(nums)
