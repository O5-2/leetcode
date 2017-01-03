class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1
        for i in dd:
            if dd[i] != 1:
                return True
        return False
