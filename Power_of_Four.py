class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while bool(1):
            if num == 0:
                return bool(0)
            if num == 1:
                return bool(1)
            current = num % 4
            if current != 0:
                return bool(0)
            else:
                num = num / 4
                if num == 1:
                    return bool(1)
