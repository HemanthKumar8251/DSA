class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.combinationsSum(candidates,target,[],0,result,0)
        return result

    def combinationsSum(self, candidates, target, combi, sum, result, idx):
        if sum>target:
            return
        elif sum==target:
            result.append(combi[:])
            return
        for i in range(idx,len(candidates)):
            combi.append(candidates[i])
            sum += candidates[i]
            self.combinationsSum(candidates,target,combi,sum,result,i)
            combi.pop()
            sum -= candidates[i]