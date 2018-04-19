class Solution:
    def replaceWords(self, dictionary, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dictionary = sorted(dictionary)
        sent = sentence.split(" ")
        for i in range(0, len(sent)):
            root = sent[i]
            for j in dictionary:
                if sent[i][:len(j)] == j:
                    root = j
                    break
            sent = sent[:i]+[root]+sent[i+1:]
        return " ".join(sent)
