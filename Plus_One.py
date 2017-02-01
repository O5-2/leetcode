class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            if digits[0] == 9:
                return [1,0]
            else:
                return [digits[0] + 1]
        number = 0
        exponent = 0
        for i in range(len(digits)-1,-1,-1):
            number += (digits[i]*(10**exponent))
            exponent += 1
        number += 1
        digits_plus_one = [int(i) for i in str(number)]
        return digits_plus_one
