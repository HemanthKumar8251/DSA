class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def partitionPalindrome(s,idx,path):
            if idx==len(s):
                result.append(path[:])
                return
            for i in range(idx,len(s)):
                if isPalindrome(s,idx,i):
                    path.append(s[idx:i+1])
                    partitionPalindrome(s,i+1,path)
                    path.pop()
        def isPalindrome(s,start,end):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        partitionPalindrome(s,0,[])
        return result