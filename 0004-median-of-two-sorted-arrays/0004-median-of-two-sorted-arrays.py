class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list1=[]
        for i in nums1:
            list1.append(i)
        for i in nums2:
            list1.append(i)
        list1.sort()
        return list1[len(list1)/2] if len(list1)%2!=0 else float(float((list1[len(list1)/2])+float(list1[(len(list1)/2)-1]))/2)
        