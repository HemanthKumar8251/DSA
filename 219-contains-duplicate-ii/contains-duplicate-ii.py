class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i],[])+[i]
        
        for _,idx in hashMap.items():
            if len(idx)>=2:
                for i in range(len(idx)-1):
                    if idx[i+1]-idx[i]<=k:
                        return True

        return False