class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = 3037000500
        if x == 0:
            return 0
        if x == 1:
            return 1
        while low < high:
            mid = (low+high)/2
            current = mid**2
            if current > x:
                if (mid-1)**2 < x:
                    return mid-1
                high = mid
            elif current < x:
                low = mid + 1
            else:
                return mid
