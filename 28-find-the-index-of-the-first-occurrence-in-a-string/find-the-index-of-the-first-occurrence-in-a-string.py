class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        i=0
        while i<=m-n:
            if haystack[i:i+n]==needle:
                return i
            i+=1
        return -1