class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n/2 + 4
        if n == 0:
            return 0
        if n == 1:
            return 1
        while low < high:
            mid = (low+high)/2
            current = ((mid+1)*mid)/2
            if current > n:
                high = mid
            elif current < n:
                if n < (((mid+1)+1)*(mid+1))/2:
                    return mid
                else:
                    low = mid + 1
            else:
                return mid
