class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> numsSet(nums.begin(), nums.end());
        return numsSet.size() < nums.size();        
    }
};