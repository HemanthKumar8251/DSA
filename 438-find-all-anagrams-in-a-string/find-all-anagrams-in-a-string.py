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

        # # O(m) Time, O(n) Space
        # for i in range(m):
        #     # Adding the char to the hashMap
        #     s_hash[s[i]]+=1
            
        #     # Removing the left most value as sliding window moves forward
        #     if i>=n:
        #         left_char = s[i-n]
        #         if s_hash[left_char]==1:
        #             del s_hash[left_char]
        #         else:
        #             s_hash[left_char]-=1
            
        #     # Addin to the reuslt
        #     if p_hash == s_hash:
        #         result.append(i-n+1)
        
        # Reducing the time for Comparision replacing hash Map
        # Comparision with match varaible comparision
        matches = 0
        required_matches = len(p_hash)
        for i in range(m):
            right_char = s[i]
            s_hash[right_char] += 1

            # Matches is only incremented if the frequency of that number is equal
            if right_char in p:
                if s_hash[right_char] == p_hash[right_char]:
                    matches += 1
                elif s_hash[right_char] == p_hash[right_char]+1:
                    matches -= 1
            
            if i>=n:
                left_char = s[i-n]
                if left_char in p_hash and s_hash[left_char] == p_hash[left_char]:
                    matches-=1
                s_hash[left_char]-=1
                if left_char in p_hash and s_hash[left_char] == p_hash[left_char]:
                    matches+=1
                    
            if matches==required_matches:
                result.append(i-n+1)

        return result
                