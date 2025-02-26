class Solution {
    public boolean isPalindrome(int x) {
        int n;
        int sum=0;
        int temp=x;
        while(x>0)
        {
            n=x%10;
            sum=sum*10+n;
            x=x/10;
        
        }
        if(sum==temp)
            return true;
        else
            return false;
    }
}