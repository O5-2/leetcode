class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        goats = []
        for i in range(0, len(words)):
            current = words[i]
            if current[0] in "aeiouAEIOU":
                current = current+"ma"
            else:
                current = current[1:]+current[0]+"ma"
            goats.append(current+("a"*(i+1)))
        return " ".join(goats)
