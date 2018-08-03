# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        while a == 7:
            a = rand7()
        b = rand7()
        while (b == 6) or (b == 7):
            b = rand7()
        return b+((a%2)*5)
