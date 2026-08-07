class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}
        for ch in magazine:
            hashMap[ch]=hashMap.get(ch,0)+1
        for ch in ransomNote:
            if hashMap.get(ch,0)==0:
                return False
            hashMap[ch]-=1
        return True