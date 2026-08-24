class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(cur_arr,i):
            if i==len(nums):
                res.append(list(cur_arr))
                return
            cur_arr.append(nums[i])
            backtracking(cur_arr,i+1)
            cur_arr.pop()
            backtracking(cur_arr,i+1)
        backtracking([],0)
        return res
