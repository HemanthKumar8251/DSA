class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Restrictions Failed
        # Line res += temp*(10**(i)): The variable 'res' accumulates the full product as an arbitrary-precision Python integer.
        # res = 0
        # n = len(num1)
        # m = len(num2)
        # for i in range(m):
        #     curr = int(num2[m-1-i])
        #     temp = 0
        #     for j in range(n-1,-1,-1):
        #         temp += int(num1[j])*curr*(10**(n-j-1))
        #     res += temp*(10**(i))
        # return str(res)

        if num1=='0' or num2=='0':
            return '0'
        m = len(num1)
        n = len(num2)
        pos = [0]*(n+m)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul = int(num1[i])*int(num2[j])
                p1,p2=i+j,i+j+1
                total = mul+pos[p2]
                pos[p1] += total//10
                pos[p2] = total%10

        result = []
        for num in pos:
            if not (num==0 and len(result)==0):
                result.append(str(num))
        return ''.join(result)
