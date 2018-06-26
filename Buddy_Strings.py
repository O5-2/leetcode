class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        letters = []
        duplicate = False
        problems = []
        for i in range(0, len(A)):
            if A[i] in letters:
                duplicate = True
            else:
                letters.append(A[i])
            if A[i] != B[i]:
                problems.append(i)
        if (len(problems) == 0 and duplicate == True):
            return True
        elif ((len(problems) == 2) and (B[problems[0]] == A[problems[1]] and B[problems[1]] == A[problems[0]])):
            return True
        else:
            return False
