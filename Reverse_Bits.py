class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        power = 0
        ans = 0
        while n != 0:
            if (n/(2**power))%2 == 1:
                ans += 2**(31-power)
                n -= 2**power
            power += 1
        return ans
