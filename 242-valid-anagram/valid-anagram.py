class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Comparing the 2 strings after coverting into a list and sorting 
        # s = list(s)
        # t = list(t)
        # s.sort()
        # t.sort()
        # return s==t

        #Hashing
        if len(s)!=len(t):
            return False
        hash_map = {}
        for i in s:
            # if i in hash_map:
            #     hash_map[i]+=1
            # else:
            #     hash_map[i]=1
            hash_map[i] = hash_map.get(i,0)+1
                
        for i in t:
            if i not in hash_map or hash_map[i]==0:
                return False
            hash_map[i]-=1
        
        # for i in hash_map.values():
        #     if i!= 0:
        #         return False

        return True

        # Using Constant Space
        # Considering the ASCII values of the alphabets
        # Given - s and t consist of lowercase English letters
        # a=97,z=122,z-a=25
        # idx(alphabet) = ord(alphabet)-ord('a')
        # if len(s)!=len(t):
        #     return False
        # letter_count = [0]*26
        
        # for i in s:
        #     letter_count[ord(i)-ord('a')]+=1
        
        # for i in t:
        #     j = ord(i)-ord('a')
        #     if letter_count[j]==0:
        #         return False
        #     letter_count[j]-=1
        
        # return True