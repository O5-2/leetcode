class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dom = [""]
        index = 2001
        for i in range(0, len(list1)):
            if list1[i] in list2:
                for j in range(0, len(list2)):
                    if (list1[i] == list2[j]) and (i+j < index):
                        dom = [list1[i]]
                        index = i+j
                    elif (list1[i] == list2[j]) and (i+j == index):
                        dom.append(list1[i])
        return dom
