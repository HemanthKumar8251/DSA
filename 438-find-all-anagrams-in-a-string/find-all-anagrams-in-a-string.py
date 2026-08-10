class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # O(mxn) Time and O(m+n) Space
        # n = len(p)
        # m = len(s)
        # hashP = Counter(p)
        # result = []
        # for i in range(m-n+1):
        #     if s[i] not in p:
        #         continue
        #     if hashP==Counter(s[i:i+n]):
        #         result.append(i)
        # return result
        m = len(s)
        n = len(p)
        if n>m:
            return []
        
        p_hash = Counter(p)
        s_hash = Counter()
        result = []
        for i in range(m):
            # Adding the char to the hashMap
            s_hash[s[i]]+=1
            
            # Removing the left most value as sliding window moves forward
            if i>=n:
                left_char = s[i-n]
                if s_hash[left_char]==1:
                    del s_hash[left_char]
                else:
                    s_hash[left_char]-=1
            
            # Addin to the reuslt
            if p_hash == s_hash:
                result.append(i-n+1)
        
        return result
                