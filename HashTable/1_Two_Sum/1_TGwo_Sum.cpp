class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res{-1, -1};
        unordered_map<int, size_t> hash;        
        for( size_t i = 0; i<nums.size(); ++i )
        {
            unordered_map<int, size_t>::const_iterator got = hash.find(target-nums[i]);
            if ( got == hash.end() )
            {
                hash.insert(std::make_pair(nums[i], i));     
            }
            else
            {
                res[0] = i;
                res[1] = got->second;         
            }                    
        }
        return res;
    }
};
