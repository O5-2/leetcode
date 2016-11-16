class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        if num == 0:
            return "0"
        elif num < 0:
            num = 4294967296 + num
            while bool(1):
                current = num % 16
                if current >= 10:
                    ans = chr(current + 87) + ans
                else:
                    if num - current == 0:
                        if num/16 <= 1:
                            ans = str(current) + ans
                    else:
                        ans = str(current) + ans
                num -= current
                if num == 0:
                    break
                else:
                    num /= 16
        elif num > 0:
            while bool(1):
                current = num % 16
                if current >= 10:
                    ans = chr(current + 87) + ans
                else:
                    if num - current == 0:
                        if num/16 <= 1:
                            ans = str(current) + ans
                    else:
                        ans = str(current) + ans
                num -= current
                if num == 0:
                    break
                else:
                    num /= 16
        return ans
