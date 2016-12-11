class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set([])
        for i in range(0, len(nums)):
            if nums[i] in set1:
                set1.remove(nums[i])
            else:
                set1.add(nums[i])
        i = iter(set1)
        return i.next()
