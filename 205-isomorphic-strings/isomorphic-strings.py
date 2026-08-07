class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for i,j in zip(s,t):
            if i in sMap and sMap[i]!=j:
                return False
            if j in tMap and tMap[j]!=i:
                return False
            sMap[i] = j
            tMap[j] = i
        return True