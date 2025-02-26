class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int n;
        int sum=0;
        int temp=x;
        while(x>0)
        {
            n=x%10;
            sum=sum*10+n;
            x=x/10;
        
        }
        return temp==sum;
    }
}