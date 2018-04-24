class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        indexToInts = {0: 1000, 1: 900, 2: 500, 3: 400, 4: 100, 5: 90, 6: 50, 7: 40, 8: 10, 9: 9, 10: 5, 11: 4, 12: 1}
        intsToNumerals = {1: 'I', 900: 'CM', 5: 'V', 1000: 'M', 9: 'IX', 10: 'X', 400: 'CD', 40: 'XL', 50: 'L', 500: 'D', 100: 'C', 90: 'XC', 4: 'IV'}
        for i in indexToInts:
            if num >= indexToInts[i]:
                return intsToNumerals[indexToInts[i]]+Solution.intToRoman(self, num-indexToInts[i])
                break
        return ""
