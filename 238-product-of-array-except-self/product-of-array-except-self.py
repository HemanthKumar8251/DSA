class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix,suffix = 1,1
        answer = [1]*n
        if nums.count(0)>=2:
            return [0]*n
        for i in range(1,n):
            prefix *= nums[i-1]
            answer[i] = prefix
        for i in range(n-2,-1,-1):
            suffix *= nums[i+1]
            answer[i] *= suffix
        return answer