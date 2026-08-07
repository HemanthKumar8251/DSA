class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # patternMap = {}
        # sMap = {}
        # for i,j in zip(pattern,t):
        #     if (i in sMap and sMap[i]!=j) or (j in tMap and tMap[j]!=i):
        #         return False
        #     sMap[i] = j
        #     tMap[j] = i
        # return True

        # Usig sets and checking for exact pairs
        if len(pattern)!=len(s.split()):
            return False
        return len(set(pattern)) == len(set(s.split())) == len(set(zip(pattern,s.split())))