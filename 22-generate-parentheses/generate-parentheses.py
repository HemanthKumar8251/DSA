class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(opened,closed,s):
            if opened==closed==n:
                res.append("".join(s))
                return
            if opened < closed:
                return
            if opened > n or closed > n:
                return
            s.append('(')
            dfs(opened+1,closed,s)
            s.pop()
            s.append(')')
            dfs(opened,closed+1,s)
            s.pop()
            
        res = []
        dfs(0,0,[])
        return res