class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        isNegative=False
        
        if x<0:
            isNegative=True
            x=-x
        while x:
            n=x%10
            rev=rev*10+n
            x=x/10
        
        if rev<-2**31 or rev>2**31-1:
            return 0

        return -rev  if isNegative else rev

            