class Solution:
    def myAtoi(self, s: str) -> int:
        #constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        #removing the leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        #checking the sign
        i = 0
        n = len(s)
        sign = 1
        if s[i] == '+':
            i+=1
        elif s[i] == '-':
            sign = -1
            i+=1
        #skiping leading zeroes
        while i<n and s[i]==0:
            i+=1
        #reading the integer skipping the leading zeros
        res = 0
        while i<n and s[i].isdigit():
            digit = int(s[i])
            res = res*10 + digit
            if sign*res <= INT_MIN:
                return INT_MIN
            if sign*res >=INT_MAX:
                return INT_MAX
            i+=1
        return sign*res          
