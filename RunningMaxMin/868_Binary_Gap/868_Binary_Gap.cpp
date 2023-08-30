class Solution {
public:
    int binaryGap(int n) {
        
        bitset<32> x(n);
        string binary = x.to_string();
        
        if(binary.length() < 2)
            return 0;
        
        int max_gap = 0;
        int last_one_pos = -1;          // Use an integer variable and set it to -1 as an indicator for "not set"
        for( int i = 0; i < binary.length(); i++ ){
            if(binary[i] == '1'){
                if(last_one_pos != -1)
                    max_gap = max( max_gap, i-last_one_pos);
                last_one_pos = i;     
            }         
        }
        return max_gap;
    }
};
