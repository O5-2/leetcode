class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return bool(0)
        if num == 1:
            return bool(1)
        while bool(1):
            bool1 = bool(0)
            if num == 1:
                return bool(1)
            if num % 2 == 0:
                bool1 = bool(1)
                num /= 2
            elif num % 3 == 0:
                bool1 = bool(1)
                num /= 3
            elif num % 5 == 0:
                bool1 = bool(1)
                num /= 5
            if bool1 == bool(0):
                return bool(0)
