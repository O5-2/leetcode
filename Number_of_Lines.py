class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        line = 0
        for i in S:
            line += widths[ord(i)-97]
            if line > 100:
                lines += 1
                line = widths[ord(i)-97]
        return [lines, line]
