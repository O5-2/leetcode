class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(numbers)):
            low = i
            high = len(numbers)-1
            if numbers[low] + numbers[high] == target:
                return [low+1,high+1]
            while low < high:
                mid = (low+high)/2
                current = numbers[mid]
                if current+numbers[i] > target:
                    high = mid
                elif current+numbers[i] < target:
                    low = mid + 1
                else:
                    if i != mid:
                        return [i+1,mid+1]
