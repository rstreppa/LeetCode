class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
    
        sort(nums.begin(), nums.end());
        int remain = k;
        int n = nums.size();
        for(unsigned int i = 0; i < min(n,k); i++) {
            if(nums[i] >=0)
                break;
            nums[i] = -nums[i];
            remain--;
        }
        return accumulate(nums.begin(),nums.end(),0) - *min_element(nums.begin(), nums.end())*(remain%2)*2;


    }
};
