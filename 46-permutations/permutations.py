class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        cur_arr = []
        used = defaultdict(bool)
        def permutations():
            if len(cur_arr)==n:
                result.append(list(cur_arr))
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i]=True
                cur_arr.append(nums[i])
                permutations()
                cur_arr.pop()
                used[i]=False
        
        permutations()
        return result