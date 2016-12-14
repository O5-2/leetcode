class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        if n <= 26:
            return chr(n+64)
        else:
            while bool(1):
                if n <= 26:
                    ans = chr(n+64) + ans
                    return ans
                elif n % 26 == 0:
                    ans = "Z" + ans
                    n -= 26
                    n /= 26
                else:
                    ans = chr((n%26)+64) + ans
                    n -= n%26
                    n /= 26
