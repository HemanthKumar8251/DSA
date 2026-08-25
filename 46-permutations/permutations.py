class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # result = []
        # cur_arr = []
        # used = defaultdict(bool)
        # def permutations():
        #     if len(cur_arr)==n:
        #         result.append(list(cur_arr))
        #         return
        #     for i in range(n):
        #         if used[i]:
        #             continue
        #         used[i]=True
        #         cur_arr.append(nums[i])
        #         permutations()
        #         cur_arr.pop()
        #         used[i]=False
        
        # permutations()
        # return result

        # Using a set for storing seen ele as all are unique 
        # Even if there were duplicates it helps avoid duplicate permutations
        result,perm = [],[]
        seen = set()
        self.permutation(perm,result,nums,seen)
        return result

    def permutation(self,perm,result,nums,seen):
        if len(nums)==len(perm):
            result.append(perm.copy())
            return
        for num in nums:
            if num not in seen:
                seen.add(num)
                perm.append(num)
                self.permutation(perm,result,nums,seen)
                seen.remove(num)
                perm.pop()