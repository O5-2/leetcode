class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        matrix = []
        numbers = []
        for i in nums:
            numbers.extend(i)
        for i in range(0, r):
            matrix.append(numbers[(i*c):((i+1)*c)])
        return matrix
