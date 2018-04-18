class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from math import ceil
        if answers == []:
            return 0
        numbers = []
        answers = sorted(answers)
        rabbits = 0
        for i in range(0, max(answers)+1):
            cur = 0
            for j in range(0, len(answers)):
                if i == answers[j]:
                    cur += 1
            numbers.append(cur)
        for i in range(0, len(numbers)):
            rabbits += ceil(float(numbers[i])/float(i+1))*(i+1)
        return rabbits
