class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        low = 0
        high = len(s) - 1
        ans = list(s)
        while high > low:
            if ans[low] not in vowels:
                low += 1
            if ans[high] not in vowels:
                high -= 1
            if ans[low] in vowels and ans[high] in vowels:
                store = ans[low]
                ans[low] = ans[high]
                ans[high] = store
                low += 1
                high -= 1
        return "".join(ans)
