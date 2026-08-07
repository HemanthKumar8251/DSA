class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # M length of magazine and N length of ransomNote
        # O(M+N) Time, O(M) Space
        hashMap = {}
        for ch in magazine:
            hashMap[ch]=hashMap.get(ch,0)+1
        for ch in ransomNote:
            if hashMap.get(ch,0)==0:
                return False
            hashMap[ch]-=1
        return True

        # O(M+N) Time, O(M+N) Space
        # st1, st2 = Counter(ransomNote), Counter(magazine)
        # if st1 & st2 == st1:
        #     return True
        # return False