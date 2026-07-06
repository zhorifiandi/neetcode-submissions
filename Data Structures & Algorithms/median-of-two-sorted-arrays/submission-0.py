class Solution:
    def getKth(self, nums1, nums2, k):
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        if len(nums1) == 0:
            return nums2[k - 1]
        
        if k == 1:
            return min(nums1[0], nums2[0])
        
        i = min(k // 2, len(nums1))
        j = min(k // 2, len(nums2))

        if nums1[i-1] < nums2[j-1]:
            return self.getKth(nums1[i:], nums2, k - i)
        else:
            return self.getKth(nums1, nums2[j:], k - j)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        nums1 = [1,3,5,7,9], nums2 = [2,4,6,8]
        median -> the (m+n) // 2 th => medianIndex = 4
        l1, r1 = 0, 4
        l2, r2 = 0, 3
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        k = (m + n + 1) // 2
        if (m + n) % 2 == 1:
            return self.getKth(nums1, nums2, k)
        else:
            return float(
                (self.getKth(nums1, nums2, k) + self.getKth(nums1, nums2, k + 1)) / 2
            )

        