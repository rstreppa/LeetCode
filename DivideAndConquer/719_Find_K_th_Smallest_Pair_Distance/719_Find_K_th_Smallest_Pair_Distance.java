class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int left = 0;
        int right = Math.abs(nums[n-1]-nums[0]);
        while(left < right) {
            int mid = left + (right-left)/2;
            int i = 0;
            int j = 1;
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
}