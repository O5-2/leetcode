class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while True:
            if bits[0] == 0:
                bits = bits[1:]
                if bits == []:
                    return True
            elif bits[0] == 1:
                bits = bits[2:]
                if bits == []:
                    return False
