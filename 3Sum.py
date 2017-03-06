class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []
        ans = []
        set1 = set()
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                for k in range(0, len(nums)):
                    if (i != j) and (j != k) and (i != k):
                        cur = [nums[i],nums[j],nums[k]]
                        sort = sorted([nums[i],nums[j],nums[k]])
                        str1 = "%s-%s-%s" % (sort[0], sort[1], sort[2])
                        if sum(cur) == 0:
                            if str1 not in set1:
                                ans.append(cur)
                                set1.add(str1)
        return ans
