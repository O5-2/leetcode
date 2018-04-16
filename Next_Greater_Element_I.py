class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nums3 = []
        for i in range(0, len(findNums)):
            found = False
            for j in range(0, len(nums)):
                if (found == True) and (findNums[i] < nums[j]):
                    nums3.append(nums[j])
                    break
                if findNums[i] == nums[j]:
                    found = True
            if len(nums3) == i:
                nums3.append(-1)
        return nums3
