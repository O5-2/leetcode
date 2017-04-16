def numDigits(n):
    ans = 0
    while n != 0:
        n /= 10
        ans += 1
    return ans

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        i = 1
        count = 0
        while count < n:
            count += numDigits(i)
            i += 1
        j = (count-n)+1
        return ((i-1)%(10**j))/(10**(j-1))

s = Solution()
print s.findNthDigit(100000000)
