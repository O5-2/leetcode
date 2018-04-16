class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        from math import sqrt
        div = [1]
        for i in range(2, (int(sqrt(num)))+1):
            if num%i == 0:
                div.append(i)
                div.append(num/i)
        return sum(div) == num
