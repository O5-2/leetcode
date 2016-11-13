class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans = ""
        if abs(a) > abs(b):
            if a < b:
                a = a * int(''.join([chr(45), str(1)]))
                b = b * int(''.join([chr(45), str(1)]))
                if a < 0:
            #stuff here
        elif abs(a) < abs(b):
            #stuff here
        elif abs(a) == abs(b):
            if a < 0:
                return 0
            elif b < 0:
                return 0
            else:
                for i in range(0, a):
                    ans = ''.join([ans, "*"])
                for i in range(0, b):
                    ans = ''.join([ans, "*"])
                return len(ans)
        #for i in range(0, a):
        #    ans = ''.join([ans, "*"])
        #for i in range(0, b):
        #    ans = ''.join([ans, "*"])
        #return len(ans)
