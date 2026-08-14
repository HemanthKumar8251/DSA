class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(s) for s in "".join([str(x) for x in nums]).split('0')])