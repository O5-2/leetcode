class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(J)
        stones = 0
        for i in S:
            if i in J:
                stones += 1
        return stones
