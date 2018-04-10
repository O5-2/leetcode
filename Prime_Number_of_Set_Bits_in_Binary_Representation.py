class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = 0
        primeBits = set([2, 3, 5, 7, 11, 13, 17, 19])
        for i in range(L, R+1):
            bits = 0
            for j in bin(i):
                if j == "1":
                    bits += 1
            if bits in primeBits:
                primes += 1
        return primes
