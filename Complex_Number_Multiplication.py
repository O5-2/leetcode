class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        A = a.split("+")
        B = b.split("+")
        f = int(A[0])*int(B[0])
        o = int(A[0])*int(B[-1][:len(B[-1])-1])
        i = int(A[-1][:len(A[-1])-1])*int(B[0])
        l = -1*int(A[-1][:len(A[-1])-1])*int(B[-1][:len(B[-1])-1])
        return str(f+l)+"+"+str(o+i)+"i"
