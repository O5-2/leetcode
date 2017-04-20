class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        nums.sort()
        low = 0
        high = 1
        ans = 0
        unique = set()
        while True:
            if high == len(nums):
                low += 1
                high = low
                if low == len(nums):
                    return ans
            elif low != high:
                tup = (nums[low],nums[high])
                if nums[high] - nums[low] == k and tup not in unique:
                    ans += 1
                    unique.add(tup)
                elif nums[high] - nums[low] > k:
                    low += 1
                    high = low
            high += 1
