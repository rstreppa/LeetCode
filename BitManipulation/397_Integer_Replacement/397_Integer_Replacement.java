class Solution {
    public int integerReplacement(int n) {
        long np = (long) n;  // Cast to long to avoid overflow
        int count = 0;
        while( np != 1 ){
            if(np % 2 == 0)
                np >>= 1;  // Equivalent to n /= 2
            else if( np == 3 ||  np % 4 == 1)
                np--;
            else
                np++;
            count += 1;
        }
        return count;
    }        
}
