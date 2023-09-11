class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> current;
        vector<vector<int>> res;
        backtrack(0, current, res, nums);
        return res;
    }
private: 
    void backtrack(size_t start, vector<int>& current, vector<vector<int>>& res, vector<int>& nums) {
        res.push_back(current);
        for( size_t i=start; i<nums.size(); i++) {
            if(i>start && nums[i] == nums[i-1])
                continue;
            current.push_back(nums[i]);
            backtrack(i+1, current, res, nums);
            current.pop_back();
        }
    }
};
