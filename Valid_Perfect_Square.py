class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 0
        high = 3037000500
        if num == 1:
            return True
        while low < high:
            mid = (low+high)/2
            guess = mid**2
            if guess > num:
                high = mid
            elif guess < num:
                low = mid + 1
            else:
                return True
        return False
