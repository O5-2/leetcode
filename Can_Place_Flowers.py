class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowers = 0
        bed = flowerbed
        if len(bed) == 1:
            if ((bed == [0]) and (n <= 1)) or ((bed == [1]) and (n == 0)):
                return True
            else:
                return False
        if (bed[0] == 0) and (bed[1] == 0):
            bed = [1] + bed[1:]
            flowers += 1
        for i in range(1, len(bed)-1):
            if ((bed[i-1] == 0) and (bed[i+1] == 0)) and (bed[i] == 0):
                bed = bed[:i] + [1] + bed[i+1:]
                flowers += 1
        if (bed[len(bed)-2] == 0) and (bed[len(bed)-1] == 0):
            bed = bed[:len(bed)-1] + [1]
            flowers += 1
        if flowers >= n:
            return True
        else:
            return False
