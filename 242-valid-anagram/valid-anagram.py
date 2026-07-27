class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Comparing the 2 strings after coverting into a list and sorting 
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s==t

        #Hashing 