class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = []
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    bool1 = bool(1)
                    for k in range(0, len(inter)):
                        if nums1[i] == inter[k]:
                            bool1 = bool(0)
                    if bool1:
                        inter.append(nums1[i])
        return inter
