class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        m = len(s)
        hashP = Counter(p)
        result = []
        for i in range(m-n+1):
            if s[i] not in p:
                continue
            if hashP==Counter(s[i:i+n]):
                result.append(i)
        return result