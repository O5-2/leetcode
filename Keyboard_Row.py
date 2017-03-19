class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"]
        ans = []
        for i in range(0,len(words)):
            one_row = True
            for j in range(0,len(rows)):
                if words[i][0] in rows[j]:
                    current = j
            for j in range(1,len(words[i])):
                if words[i][j] not in rows[current]:
                    one_row = False
            if one_row == True:
                ans.append(words[i])
        return ans
