class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Using Back Tracking (Recursion)
        res = []
        def backtracking(cur_arr,i):
            if i==len(nums):
                if sorted(cur_arr) not in res:
                    res.append(list(sorted(cur_arr)))
                return
            cur_arr.append(nums[i])
            backtracking(cur_arr,i+1)
            cur_arr.pop()
            backtracking(cur_arr,i+1)
        backtracking([],0)
        return res
