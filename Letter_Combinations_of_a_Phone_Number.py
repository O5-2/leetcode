class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if digits == "":
            return []
        if len(digits) == 1:
            return [i for i in mapping[int(digits[0])]]
        cur = []
        for i in mapping[int(digits[0])]:
            cur += [i+j for j in self.letterCombinations(digits[1:])]
        return cur
