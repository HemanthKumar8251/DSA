class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort - O(nlogn) Time,O(n) Space
        def mergeSort(nums,low,high):
            if low==high:
                return
            mid = (low+high)//2
            mergeSort(nums,low,mid)
            mergeSort(nums,mid+1,high)
            merge(nums,low,mid,high)
        def merge(nums,low,mid,high):
            left=low
            right=mid+1
            temp = []
            while left<=mid and right<=high:
                if nums[left]<nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while left<=mid:
                    temp.append(nums[left])
                    left+=1
            while right<=high:
                    temp.append(nums[right])
                    right+=1
            for i in range(low,high+1):
                nums[i]=temp[i-low]

        mergeSort(nums,0,len(nums)-1)
        return nums

        # # Quick Sort - O(nlogn) Avg Case /O(n^2) Worst Case Time
        # # O(nlogn) Space, O(n) Worst Case
        # def quickSort(nums,low,high):
        #     if low<high:
        #         prt_idx = partition(nums,low,high)
        #         quickSort(nums,low,prt_idx-1)
        #         quickSort(nums,prt_idx+1,high)
        
        # def partition(nums,low,high):
        #     pivot = nums[low]
        #     left,right = low,high
        #     while left<right:
        #         while left<=high-1 and nums[left]<=pivot:
        #             left+=1
        #         while right>=low+1 and nums[right]>pivot:
        #             right-=1
        #         if left<right:
        #             nums[left],nums[right]=nums[right],nums[left]
        #     nums[low],nums[right]=nums[right],nums[low]
        #     return left
        
        # quickSort(nums,0,len(nums)-1)
        # return nums