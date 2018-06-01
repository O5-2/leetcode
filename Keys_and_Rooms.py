class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        oldKeys = rooms[0]
        keys = [0]
        for i in oldKeys:
            keys += rooms[i]
        keys = list(set(keys))
        while keys != oldKeys:
            oldKeys = keys
            keys = [0]
            for i in oldKeys:
                keys += rooms[i]
            keys = list(set(keys))
        n = len(rooms)
        return sum(keys) == int(n*(n-1)/2)
