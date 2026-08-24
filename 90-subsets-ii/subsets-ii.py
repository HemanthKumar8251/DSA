class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Using Back Tracking (Recursion)
        nums = sorted(nums)
        res = []
        def backtracking(cur_arr,i):
            if i==len(nums):
                if cur_arr not in res:
                    res.append(list(cur_arr))
                return
            cur_arr.append(nums[i])
            backtracking(cur_arr,i+1)
            cur_arr.pop()
            while i+1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(cur_arr,i+1)
        backtracking([],0)
        return res
