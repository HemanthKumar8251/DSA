class Solution:
    def countAndSay(self, n: int) -> str:
        # Iterative Approach
        # res = '1'
        # for i in range(n-1):
        #     count = 1
        #     temp = ''
        #     for j in range(1,len(res)):
        #         if res[j]==res[j-1]:
        #             count += 1
        #         else:
        #             temp += str(count)+res[j-1]
        #             count = 1
        #     temp += str(count)+res[-1]
        #     res = temp
        # return res

        #Recursive Approach
        if n==1:
            return '1'
        prev = self.countAndSay(n-1)
        res =''
        count = 1
        for j in range(1,len(prev)):
            if prev[j]==prev[j-1]:
                count += 1
            else:
                res += str(count)+prev[j-1]
                count = 1
        res += str(count)+prev[-1]
        return res