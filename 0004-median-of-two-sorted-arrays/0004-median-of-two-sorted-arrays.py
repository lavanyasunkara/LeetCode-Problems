class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list1=nums1+nums2
        list1.sort()
        n=len(list1)
        return list1[n/2] if n%2!=0 else (float(list1[n/2])+float(list1[n/2-1]))/2