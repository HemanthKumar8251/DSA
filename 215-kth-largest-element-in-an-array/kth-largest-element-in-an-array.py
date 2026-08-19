class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ## Using max heap and poping until k ele
        # nums = [-x for x in nums]
        # heapq.heapify(nums)
        # print(nums)
        # for i in range(k-1):
        #     heapq.heappop(nums)
        # return -1*heapq.heappop(nums)

        ## Using min heap and sorting only k largest elements
        # heap = nums[:k]
        # heapq.heapify(heap)
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        # return heap[0]

        # ## Using quick select 2way partition - Time Limit Exceeded 
        # def quickSelect(nums,low,high):
        #     if low<=high:
        #         prt_idx = partition(nums,low,high)
        #         if prt_idx==len(nums)-k:
        #             return nums[prt_idx]
        #         elif prt_idx<len(nums)-k:
        #             return quickSelect(nums,prt_idx+1,high)
        #         else:
        #             return quickSelect(nums,low,prt_idx-1)
        # def partition(nums,low,high):
        #     pivot_idx = random.randint(low, high)
        #     nums[low],nums[pivot_idx]=nums[pivot_idx],nums[low]
        #     pivot = nums[low]
        #     i,j = low,high
        #     while i<j:
        #         while i<=high-1 and nums[i]<=pivot:
        #             i+=1
        #         while j>=low+1 and nums[j]>pivot:
        #             j-=1
        #         if i<j:
        #             nums[i],nums[j]=nums[j],nums[i]
        #     nums[low],nums[j]=nums[j],nums[low]
        #     return j
        # return quickSelect(nums,0,len(nums)-1)

        # # Quick select 3-way partition and extra space
        # if not nums: return
        # pivot = random.choice(nums)
        # lt = [x for x  in nums if x<pivot]
        # eq = [x for x  in nums if x==pivot]
        # gt = [x for x  in nums if x>pivot]
        # L,M = len(gt), len(eq)

        # if k<=L:
        #     return self.findKthLargest(gt,k)
        # elif k>L+M:
        #     return self.findKthLargest(lt,k-L-M)
        # else:
        #     return eq[0]

        # 3-way Quick Select in-place:
        target_idx = len(nums)-k

        def quickSelect(low,high):
            if low>=high:
                return nums[low]
            
            pivot_idx = random.randint(low,high)
            pivot = nums[pivot_idx]

            i = low
            lt = low
            gt = high

            while i<=gt:
                if nums[i]<pivot:
                    nums[i],nums[lt]=nums[lt],nums[i]
                    lt+=1
                    i+=1
                elif nums[i]>pivot:
                    nums[i],nums[gt]=nums[gt],nums[i]
                    gt-=1
                else:
                    i+=1

            if target_idx<lt:
                return quickSelect(low,lt-1)
            elif target_idx>gt:
                return quickSelect(gt+1,high)
            else:
                return nums[target_idx]

        return quickSelect(0,len(nums)-1)