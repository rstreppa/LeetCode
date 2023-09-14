class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        size_t n = nums.size();
        int left = 0;
        int right = abs(nums[n-1]-nums[0]);
        while(left < right) {
            int mid = left + (right-left)/2;
            size_t i = 0;
            size_t j = 1;
            int count = 0;
            while(i < n) {
                while(j < n && nums[j] - nums[i] <= mid)
                    j++;
                count += j - i - 1;
                i++;
            }
            if(count >= k)
                right = mid;
            else
                left = mid + 1;
        }
        return right;
    }
};