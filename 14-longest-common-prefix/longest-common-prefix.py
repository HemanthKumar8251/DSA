class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Using extra space to store results
        strs.sort()
        res = ''
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i]!=strs[-1][i]:
                return res
            res += strs[0][i]
        return res
        # Without Extra Space
        # return res
        # if not strs:
        #     return ''
        # strs.sort()
        # first = strs[0]
        # last = strs[-1]
        # for i in range(min(len(first),len(last))):
        #     if first[i]!=last[i]:
        #         return first[:i]
        # return first[:min(len(first), len(last))]