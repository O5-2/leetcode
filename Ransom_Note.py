class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) == 0:
            return True
        if len(magazine) == 0:
            return ransomNote == ""
        if len(ransomNote) > len(magazine):
            return False
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        ransomNote.sort()
        magazine.sort()
        i = 0
        j = 0
        while True:
            if ransomNote[i] == magazine[j]:
                i += 1
                j += 1
            else:
                j += 1
            if j == len(magazine) or i == len(ransomNote):
                if i == len(ransomNote):
                    return True
                else:
                    return False
