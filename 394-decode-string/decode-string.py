class Solution:
    def decodeString(self, s: str) -> str:
        curr_str = ''
        k = 0
        st = []
        for ch in s:
            if ch=='[':
                st.append([k,curr_str])
                k = 0
                curr_str = ''
            elif ch==']':
                rep,prev_str = st.pop()
                curr_str = prev_str + curr_str*rep
            elif ch.isdigit():
                k = k*10+int(ch)
            else:
                curr_str+=ch
        return curr_str