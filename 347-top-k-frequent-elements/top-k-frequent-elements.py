class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency = {}
        # for i in nums:
        #     frequency[i]=frequency.get(i,0)+1
        
        # # Time Complexity O(nlogn)
        # sortedNums = sorted(list(frequency.items()),key=lambda x:x[1],reverse=True)
        # result = []
        # for i in range(k):
        #     result.append(sortedNums[i][0])
        # return result

        # Time Complexity O(n), Space Complexity O(n)
        counter = {}
        for i in nums:
            counter[i] = counter.get(i,0)+1
        
        freq = [[] for _ in range((len(nums)+1))]
        for num,f in counter.items():
            freq[f].append(num)
        
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
