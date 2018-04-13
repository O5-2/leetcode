class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = 0
        rounds = []
        j = 0
        for i in range(0, len(ops)):
            if ops[i] == "+":
                points += rounds[j-2]+rounds[j-1]
                rounds.append(rounds[j-2]+rounds[j-1])
            elif ops[i] == "C":
                points -= rounds[j-1]
                rounds = rounds[:len(rounds)-1]
                j -= 2
            elif ops[i] == "D":
                points += 2*rounds[j-1]
                rounds.append(2*rounds[j-1])
            else:
                points += int(ops[i])
                rounds.append(int(ops[i]))
            j += 1
        return points
