class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {

        // Sort the array
        sort(nums.begin(), nums.end());

        // Initialize variables
        size_t n = nums.size();
        long  res = INT_MAX;

        for(size_t i = 0; i < n-2; i++) {
            // Initialize two pointers
            size_t left = i+1;
            size_t right = n-1;

            // Two pointers technique
            while(left < right) {
                // Calculate the current sum
                int curr = nums[i]+nums[left]+nums[right];

                // Update the result if the current sum is closer to the target
                if(abs(curr - target) < abs(res - target))
                    res = curr;

                // Move pointers
                if(curr > target)
                    right--;
                else
                    left++;
            }
        }
        return int(res);        
    }
};
