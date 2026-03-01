class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=1
        for i in range(1,len(nums)):
            
            if res==1 or nums[i]!=nums[res-2]:
                nums[res]=nums[i]
                res+=1
                
        return res
                