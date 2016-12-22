# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        if n == 1:
            return 1
        while low < high:
            mid = ((low+high)/2)
            current = isBadVersion(mid)
            if current == True:
                high = mid
            else:
                if isBadVersion(mid+1):
                    return mid+1
                low = mid + 1
