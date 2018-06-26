class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S == "()":
            return 1
        level = 0
        for i in range(0, len(S)):
            if S[i] == "(":
                level += 1
            else:
                level -= 1
            if level == 0:
                if i != len(S)-1:
                    return (self.scoreOfParentheses(S[:i+1]))+(self.scoreOfParentheses(S[i+1:]))
                else:
                    return 2*(self.scoreOfParentheses(S[1:-1]))
