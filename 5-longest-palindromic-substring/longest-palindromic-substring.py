class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==1:
            return s

        # for i in range(n-1):
        #     j=n-1
        #     while(j>i):
        #         if s[i]==s[j] and s[i:j+1]==s[i:j+1][::-1]:
        #             return s[i:j+1]
        #         j -= 1
        # return s[0]
        def expand_around_center(s: str,left: int, right: int):
            n = len(s)
            while(left>=0 and right<n and s[left]==s[right]):
                left-=1
                right+=1
            return right - left - 1
        start = 0
        end = 0
        
        for i in range(n):
            odd = expand_around_center(s,i,i)
            even = expand_around_center(s,i,i+1)
            max_len = max(odd,even)

            if max_len>end-start:
                start = i - (max_len-1)//2
                end = i + max_len//2

        return s[start:end+1]
            
        return s[res[0]:res[1]+1]