class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            frequency[i]=frequency.get(i,0)+1
        
        # Time Complexity O(nlogn)
        sortedNums = sorted(list(frequency.items()),key=lambda x:x[1],reverse=True)
        result = []
        for i in range(k):
            result.append(sortedNums[i][0])
        return result