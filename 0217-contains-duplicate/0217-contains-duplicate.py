class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        nums=set(nums)
        l= len(nums)
        if l==length:
            return False
        else:
            return True
        