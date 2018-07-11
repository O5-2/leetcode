class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) <= 1:
            return list(set([S.lower(), S.upper()]))
        a = self.letterCasePermutation(S[1:])
        z = [S[0].lower()+i for i in a]+[S[0].upper()+i for i in a]
        return list(set(z))
