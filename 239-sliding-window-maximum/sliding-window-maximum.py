class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## O(n*k) Time - Giving TLE, O(k) Space
        # res = []
        # if len(nums)==k:
        #     return [max(nums)]
        # queue = deque()
        # for right,num in enumerate(nums):
        #     queue.append(num)
        #     if right>=k-1:
        #         res.append(max(queue))
        #         queue.popleft()
        # return res

        # O(n) Time, O(k) Space
        res = []
        queue = deque()
        for right, num in enumerate(nums):
            while queue and nums[queue[-1]]<num:
                queue.pop()
            queue.append(right)
            if queue[0]<right-k+1:
                queue.popleft()
            if right>=k-1:
                res.append(nums[queue[0]])
        return res
