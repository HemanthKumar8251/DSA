class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return '0'
        st = []
        for digit in num:
            while k and st and st[-1]>digit:
                st.pop()
                k-=1
            st.append(digit)
        if k>0:
            st = st[:-k]
        res = ''.join(st).lstrip('0')
        return res if res else '0'