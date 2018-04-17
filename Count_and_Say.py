class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        cas = "11"
        for i in range(0, n-2):
            new = ""
            streak = 1
            for j in range(0, len(cas)-1):
                if cas[j] == cas[j+1]:
                    streak += 1
                else:
                    new += str(streak) + cas[j]
                    streak = 1
            if cas[len(cas)-2] != cas[len(cas)-1]:
                new += "1"+cas[len(cas)-1]
            else:
                new += str(streak)+cas[len(cas)-1]
            cas = new
        return cas
