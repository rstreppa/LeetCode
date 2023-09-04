class Solution {
    public int[] singleNumber(int[] nums) {
        
        int xor_all = 0;
        for(int num : nums)
            xor_all ^= num;

        int diff = 1;
        while((xor_all & diff)==0)
            diff <<= 1;

        int a = 0, b = 0;
        for(int num : nums){
            if((num & diff) != 0)
                a ^= num;
            else
                b ^= num;
        }
        int[] res = {a, b};
        return res;
    }
}
