class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = bin(N)[2:]
        count = 0
        for i in range(0, len(n)):
            if n[i] == "1":
                count += 1
        if count < 2:
            return 0
        pairs = []
        firstOne = -1
        for i in range(0, len(n)):
            if n[i] == "1":
                firstOne = i
                break
        begin = firstOne
        for i in range(firstOne+1, len(n)):
            if n[i] == "1":
                pairs.append(i-begin)
                begin = i
        return max(pairs)
