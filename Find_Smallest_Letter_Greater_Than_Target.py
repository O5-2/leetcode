class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        numLetters = [ord(i)-97 for i in letters]
        newLetters = []
        numTarget = ord(target)-97
        if numTarget >= max(numLetters):
            newLetters = [i+26 for i in numLetters]
        else:
            newLetters = numLetters
        diff = 100
        for i in range(0, len(newLetters)):
            if (newLetters[i] > numTarget) and (diff > newLetters[i] - numTarget):
                diff = newLetters[i] - numTarget
        if 26 <= max(newLetters):
            return chr(numTarget+diff+71)
        else:
            return chr(numTarget+diff+97)
