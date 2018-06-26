class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if "." in S:
            a = (S.lower()).split("@")
            return a[0][0]+"*****"+a[0][-1]+"@"+a[1]
        else:
            a = ""
            for i in S:
                if i in "0123456789":
                    a += i
            if len(a) == 10:
                return "***-***-"+a[-4:]
            else:
                return "+"+("*"*(len(a)-10))+"-***-***-"+a[-4:]
