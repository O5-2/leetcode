class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtype = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 15 == 0:
                    rtype.append("FizzBuzz")
                else:
                    rtype.append("Fizz")
            elif i % 5 == 0:
                rtype.append("Buzz")
            else:
                rtype.append(str(i))
        return rtype
