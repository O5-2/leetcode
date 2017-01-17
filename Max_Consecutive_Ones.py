class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = 0
        current = 0
        for i in nums:
            if i == 1:
                current += 1
            else:
                if Max <= current:
                    Max = current
                current = 0
        if Max <= current:
            return current
        else:
            return Max
