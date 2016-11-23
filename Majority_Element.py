class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        layered_list = []
        for i in range(0, len(nums)):
            bool1 = bool(0)
            for j in range(0, len(layered_list)):
                if nums[i] == layered_list[j][0]:
                    layered_list[j][1] += 1
                    bool1 = bool(1)
            if bool1 == bool(0):
                layered_list.append([nums[i], 1])
            for j in range(0, len(layered_list)):
                if layered_list[j][1] > (len(nums)/2):
                    return layered_list[j][0]
