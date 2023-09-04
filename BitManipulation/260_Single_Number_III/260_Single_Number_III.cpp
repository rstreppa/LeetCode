class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {

        int xor_all = 0;
        for( const auto& num : nums )
            xor_all ^= num;             // xor_all is a^b now          
        
        // find a set bit in xor_all
        int diff = 1;
        while( (xor_all & diff) == 0 )
            diff <<= 1;
        
        int a = 0, b = 0;
        for( const auto& num : nums ) {
            if(num&diff) {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        vector<int> res{ a, b };
        return res;
    }
};
