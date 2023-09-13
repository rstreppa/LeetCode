class Solution {
public:
    bool canJump(vector<int>& nums) {
        size_t n = nums.size();
        size_t last_pos = n-1;

        for(int i = n-1; i>=0; i--) {
            if(nums[i] + i >= last_pos)
                last_pos = i;
        }
        return last_pos == 0;
    }
};
