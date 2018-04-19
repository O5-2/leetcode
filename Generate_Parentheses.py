class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        combos = []
        recur = Solution.generateParenthesis(self, n-1)
        for i in range(0, len(recur)):
            for j in range(0, len(recur[i])+1):
                combos += [recur[i][:j]+"()"+recur[i][j:]]
        return sorted(list(set(combos)))
