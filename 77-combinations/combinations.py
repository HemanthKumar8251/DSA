class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def allCombinations(combi,idx,left):
            if left==0:
                result.append(combi[:])
                return 
            for i in range(idx,n+1):
                combi.append(i)
                allCombinations(combi,i+1,left-1)
                combi.pop()
        
        allCombinations([],1,k)
        return result