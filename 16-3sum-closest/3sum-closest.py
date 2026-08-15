class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff_sum = inf
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                curr = nums[i]+nums[j]+nums[k]
                if abs(target-curr)<abs(target-min_diff_sum):
                    min_diff_sum = curr
                if curr<target:
                    j+=1
                elif curr>target:
                    k-=1
                else:
                    return target
        return min_diff_sum