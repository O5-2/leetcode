class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para = ""
        for i in paragraph:
            if i not in "!?',;.":
                para += i
        words = {}
        for i in para.split():
            if i.lower() not in words:
                words[i.lower()] = 0
            words[i.lower()] += 1
        v=list(words.values())
        k=list(words.keys())
        while k[v.index(max(v))] in banned:
            words = {key: value for key, value in words.items() if key != k[v.index(max(v))]}
            v=list(words.values())
            k=list(words.keys())
        return k[v.index(max(v))]
