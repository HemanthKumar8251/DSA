class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0

        # O(n**4) Time, O(1) Space
        # for i in nums1:
        #     for j in nums2:
        #         for k in nums3:
        #             for l in nums4:
        #                 if i+j+k+l == 0:
        #                     count += 1


        # O(n**3) Time, O(n) Space
        # hashMap = {}
        # for i in nums4:
        #     hashMap[i] = hashMap.get(i,0)+1
        # for i in nums1:
        #     for j in nums2:
        #         for k in nums3:
        #             if -(i+j+k) in hashMap:
        #                 count += hashMap[-(i+j+k)]

        # O(n**2) Time, O(n**2) Space
        hashMap = {}
        for i in nums3:
            for j in nums4:
                hashMap[i+j] = hashMap.get(i+j,0)+1
        for i in nums1:
            for j in nums2:
                if -(i+j) in hashMap:
                    count += hashMap[-(i+j)]

        return count

        # Using built in counter for effectient building of hashMap and comprehensions
        # to reduce it into 1 line of code
        # AB = collections.Counter(a+b for a in nums1 for b in nums2)
        # return sum(AB[-c-d] for c in nums3 for d in nums4)
        