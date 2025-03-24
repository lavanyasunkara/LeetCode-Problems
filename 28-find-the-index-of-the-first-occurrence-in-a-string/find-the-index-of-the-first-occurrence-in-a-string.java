class Solution {
    public int strStr(String haystack, String needle) {
        if(haystack.length()<needle.length())
            return -1;
        if(haystack.length()==needle.length())
        {
            if(haystack.equals(needle))
                return 0;
        }
        if(needle.length()==1)
        {
            if(haystack.contains(needle))
                //char c=needle.charAt(0);
                return haystack.indexOf(needle);
        }
        for(int i=0;i<=haystack.length()-needle.length();i++)
        {
            int j=0;
            while(j<needle.length() && haystack.charAt(i+j)==needle.charAt(j))
                j++;
            if(j==needle.length()){
                return i;
            }

        }
        return -1;
    }
}