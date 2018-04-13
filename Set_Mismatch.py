class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        numbers = sorted(nums)
        s = [i for i in range(1, len(numbers)+1)]
        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i-1]:
                out.append(numbers[i])
                break
        numbers.remove(out[0])
        for i in range(0, len(numbers)):
            s.remove(numbers[i])
        return out+s
