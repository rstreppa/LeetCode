class Solution {
    public int threeSumClosest(int[] nums, int target) {
        // Sort the array
        Arrays.sort(nums);

        // Initialize variables
        int n = nums.length;
        long res = Integer.MAX_VALUE;

        for(int i = 0; i < n-2; i++) {
            // Initialize two pointers
            int left = i+1;
            int right = n-1;

            // Two pointers technique
            while(left < right) {
                // Calculate the current sum
                int curr = nums[i] + nums[left] + nums[right];

                // Update the result if the current sum is closer to the target
                if(Math.abs(curr - target) < Math.abs(res - target))
                    res = curr;

                // Move pointers
                if(curr > target)
                    right--;
                else
                    left++;
            }
        }
        return (int)res;                
    }
}