class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set([i for i in range(0,len(nums)+1)])
        t = s - set(nums)
        return list(t)[0]
