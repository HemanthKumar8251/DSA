class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(i for i in list(s) if i not in " \"\'.?:;,<>`~/|@!#$%^&*()-+_=[]{\}")
        # Using the python method isalnum() to consider only alphabet and number
        s = "".join(i for i in s if i.isalnum())
        s = s.lower()
        n = len(s)
        for i in range(n//2):
            if s[i]!=s[n-i-1]:
                return False
        return True