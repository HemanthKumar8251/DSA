class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split(' ')
        l = [x.strip() for x in l if x != '']
        l = reversed(l)
        return " ".join(l)