class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n==3:
            if sum(nums)==0:
                return [nums]
            else:
                return []
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i]==nums[i-1]:
                continue

            j = i+1
            k = n-1

            while j<k :
                ele_sum = nums[i]+nums[j]+nums[k]
                if ele_sum<0:
                    j+=1
                elif ele_sum>0:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return res