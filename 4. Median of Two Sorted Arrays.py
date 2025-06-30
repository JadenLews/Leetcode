class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        smaller = []
        bigger = []
        m = len(nums1)
        n = len(nums2)
        if m > n:
            smaller = nums2
            bigger = nums1
        else:
            smaller = nums1
            bigger = nums2

        half_len = (m + n + 1) // 2
        low = 0
        high = len(smaller)

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            maxLA = float('-inf') if i == 0 else smaller[i - 1]
            minRA = float('inf') if i == len(smaller) else smaller[i]

            maxLB = float('-inf') if j == 0 else bigger[j - 1]
            minRB = float('inf') if j == len(bigger) else bigger[j]

            if maxLA <= minRB and maxLB <= minRA:
                if (m + n) % 2 == 0:
                    return (max(maxLA, maxLB) + min(minRA, minRB)) / 2.0

                else:
                    return float(max(maxLA, maxLB))
            elif maxLA > minRB:
                high = i - 1
            else: 
                low = i + 1


        
