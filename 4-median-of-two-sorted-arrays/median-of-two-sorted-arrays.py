class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute Force Approach - O(m+n) Time
        i,j=0,0
        m,n=len(nums1),len(nums2)
        temp = []
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
        while i<m:
            temp.append(nums1[i])
            i+=1
        while j<n:
            temp.append(nums2[j])
            j+=1
        t_len = len(temp)
        if t_len%2==0:
            return (temp[t_len//2]+temp[t_len//2 - 1])/2
        else:
            return temp[t_len//2]