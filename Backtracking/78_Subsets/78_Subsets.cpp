class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> current;
        backtrack(0, current, res, nums);
        return res;
    }
private:
    void backtrack(size_t start, vector<int>& current, vector<vector<int>>& res, vector<int>& nums) {
        if(start == nums.size()) {
            res.push_back(current);
            return;
        }
        
        // Include the current element
        current.push_back(nums[start]);
        backtrack(start+1, current, res, nums);  
        
        // Exclude the current element
        current.pop_back();
        backtrack(start+1, current, res, nums);
    }
};
