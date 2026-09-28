class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_para = 0
        for ch in s:
            if ch=='(':
                count+=1
            elif ch==')':
                count-=1
            else:
                continue
            max_para = max(count,max_para)
        return max_para