class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        start = end = nums[0]
        for n in nums[1:]:
            if n-1==end:
                end = n
            else:
                if start==end:
                    res.append(str(end))
                else:
                    res.append(str(start)+"->"+str(end))
                start=end=n
        if start==end:
            res.append(str(end))
        else:
            res.append(str(start)+"->"+str(end))
        return res           