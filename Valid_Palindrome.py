class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        s = s.lower()
        to_remove = [" ",":",";",".",",","~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","<",">","{","[","}","]","?","'",'"']
        for i in to_remove:
            s = "".join(s.split(i))
        print s
        return s == s[::-1]
