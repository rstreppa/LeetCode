class Solution {
public:
    Solution(vector<int>& nums) {
        for(int i = 0; i<nums.size(); i++)
            d[nums[i]].insert(i);    
    }
    
    int pick(int target) {
        auto& s = d[target];
        int idx = rand()%s.size();
        auto it = s.begin();
        advance(it, idx);
        return *it;
    }
private:
    unordered_map<int, unordered_set<int>> d;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */