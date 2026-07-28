class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n==1:
            return 1
            
        def expand_around_center(s: str,left: int, right: int):
            n = len(s)
            count = 0
            while(left>=0 and right<n and s[left]==s[right]):
                left-=1
                right+=1
                count += 1
            return count
            
        count = 0
        for i in range(n):
            odd = expand_around_center(s,i,i)
            even = expand_around_center(s,i,i+1)
            count += odd+even

        return count