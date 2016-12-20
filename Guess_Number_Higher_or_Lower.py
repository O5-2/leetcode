# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        if guess(n) == 0:
            return n
        while low < high:
            mid = (low+high)/2
            current = guess(mid)
            if current == -1:
                high = mid
            elif current == 1:
                low = mid + 1
            else:
                return mid
