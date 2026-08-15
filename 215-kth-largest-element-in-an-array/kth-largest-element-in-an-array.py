class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ## Using max heap and poping
        nums = [-x for x in nums]
        heapq.heapify(nums)
        print(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -1*heapq.heappop(nums)

        # heap = nums[:k]
        # heapq.heapify(heap)
        
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        
        # return heap[0]