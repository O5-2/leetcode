class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans_list = list(s)
        current = ""
        i = 0
        j = len(s)-1
        while i < j:
            current = ans_list[i]
            ans_list[i] = ans_list[j]
            ans_list[j] = current
            i += 1
            j -= 1
        ans = "".join(ans_list)
        return ans
