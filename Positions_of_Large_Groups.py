class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        s = 0
        groups = []
        x = 0
        while s < len(S)-2:
            if (S[s] == S[s+1]) and (S[s+1] == S[s+2]):
                x = s
                s += 2
                while (s+1 < len(S)):
                    if (S[s] != S[s+1]):
                        break
                    s += 1
                groups.append([x, s])
            s += 1
        return groups
