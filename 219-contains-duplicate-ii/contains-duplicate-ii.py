class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # O(N**2) Time, O(N) Space
        # hashMap = {}
        # for i in range(len(nums)):
        #     hashMap[nums[i]] = hashMap.get(nums[i],[])+[i]
        
        # for _,idx in hashMap.items():
        #     if len(idx)>=2:
        #         for i in range(len(idx)-1):
        #             if idx[i+1]-idx[i]<=k:
        #                 return True
        # return False
        

        # O(N) Time, O(N) Space
        # hashMap = {}
        # for i,num in enumerate(nums):
        #     if num in hashMap and i-hashMap[num]<=k:
        #         return True
        #     hashMap[num] = i
        # return False

        # Sliding Window O(N) Time, O(min(N,K)) Space
        hashSet = set()
        for i,num in enumerate(nums):
            if len(hashSet)>k:
                hashSet.remove(nums[i-k-1])
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
            