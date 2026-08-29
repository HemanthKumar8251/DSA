class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.combinationsSum(candidates,target,[],0,result,0)
        return result

    def combinationsSum(self, candidates, target, combi, sum, result, idx):
        if sum>target:
            return
        elif sum==target:
            result.append(combi[:])
            return
        for i in range(idx,len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            combi.append(candidates[i])
            sum += candidates[i]
            self.combinationsSum(candidates,target,combi,sum,result,i+1)
            combi.pop()
            sum -= candidates[i]