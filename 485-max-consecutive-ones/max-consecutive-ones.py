class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # return max([len(s) for s in "".join([str(x) for x in nums]).split('0')])
        max_count = -1
        count = 0
        for num in nums:
            if num == 0:
                max_count = max(count,max_count)
                count = 0
            else:
                count+=1
        return max_count if max_count>count else count
            