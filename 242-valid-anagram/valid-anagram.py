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
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i] = 1
        for i in t:
            if i in hash_map:
                hash_map[i]-=1
            else:
                return False
        
        flag = any((i for i in hash_map.values()))
                
        if flag:
            return False
        return True