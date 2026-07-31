class Solution:
    def reverseWords(self, s: str) -> str:
        # Using extra space O(len(s))
        # s = s.strip()
        # l = s.split(' ')
        # l = [x.strip() for x in l if x != '']
        # l = reversed(l)
        # return " ".join(l)

        # Reduced Operations
        return " ".join(s.split()[::-1])

        # With space complexity O(1) is not possible in python as strings are immutable
