class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if -6 <= num and num <= 6:
            return str(num)
        negative = num <= 0
        ans = []
        while num != 0:
            if negative:
                current = str(-1*(num%-7))
                ans.append(current)
                num = (num+(-1*(num%-7)))/7
            else:
                current = str(num%7)
                ans.append(current)
                num = (num-(num%7))/7
        if negative:
            ans.append("-")
        ans.reverse()
        ans = ''.join(ans)
        return ans
