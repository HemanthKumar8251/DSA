class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        decreasing_mst = []
        # # This takes more time as we again need to get the 
        # # correspondin values of nums1 in nums2 and then form a result
        # greater_ele = [-1]*len(nums2)
        # for i in range(len(nums2)):
        #     while decreasing_mst and nums2[i]>=nums2[decreasing_mst[-1]]:
        #         greater_ele[decreasing_mst[-1]] = nums2[i]
        #         decreasing_mst.pop()
        #     decreasing_mst.append(i)
        
        # We use hashmap instead for easy access which increses space but reduces time
        greater_ele = {}
        for num in nums2:
            while decreasing_mst and num>=decreasing_mst[-1]:
                greater_ele[decreasing_mst.pop()]=num
            decreasing_mst.append(num)
        
        return [greater_ele.get(num,-1) for num in nums1]
