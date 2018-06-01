class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if ((rec1[2] > rec2[0]) and (rec2[0] >= rec1[0])) or ((rec2[2] > rec1[0]) and (rec1[0] >= rec2[0])):
            if ((rec1[3] > rec2[1]) and (rec2[1] >= rec1[1])) or ((rec2[3] > rec1[1]) and (rec1[1] >= rec2[1])):
                return True
            else:
                return False
        else:
            return False
