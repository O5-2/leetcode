class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return sorted(str(N)) in [sorted(str(2**i)) for i in range(0, 30)]
