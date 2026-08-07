class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)!=len(s.split()):
            return False
        patternMap = {}
        sMap = {}
        for i,j in zip(pattern,s.split()):
            if (i in patternMap and patternMap[i]!=j) or (j in sMap and sMap[j]!=i):
                return False
            patternMap[i] = j
            sMap[j] = i
        return True

        # Usig sets and checking for exact pairs
        # return len(set(pattern)) == len(set(s.split())) == len(set(zip(pattern,s.split())))