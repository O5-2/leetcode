class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str1 = str(x)
        if int(str(abs(x))[::-1]) >= 2147483648:
            return 0
        elif x < 0:
            while bool(1):
                if str1[-1] == "0":
                    str1 = str1[:-1]
                    x = int(str1)
                else:
                    break
            str1 = "-" + (str(x)[1:])[::-1]
            return int(str1)
        else:
            while bool(1):
                if str1[:-1] == "0":
                    str1 = str1[:-1]
                    x = int(str1)
                else:
                    break
            return int(str1[::-1])
