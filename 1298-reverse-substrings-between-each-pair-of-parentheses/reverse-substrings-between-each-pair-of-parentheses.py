class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        res_s = ''
        for i in s:
            if i=='(':
                st.append(res_s)
                res_s = ''
            elif i==')':
                res_s = res_s[::-1]
                res_s = st.pop()+res_s
            else:
                res_s+=i
        return res_s