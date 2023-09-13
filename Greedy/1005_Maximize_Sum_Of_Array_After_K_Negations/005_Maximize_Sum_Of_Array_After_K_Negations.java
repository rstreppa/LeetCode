class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
        int remain = k;
        int n = nums.length;
        for(int i = 0; i < Math.min(n,k); i++) {
            if(nums[i] >=0)
                break;
            nums[i] = -nums[i];
            remain--;
        }

        int minVal = Integer.MAX_VALUE;
        for(int e: nums) {
            if(e<=minVal)
                minVal = e;
        }
        return Arrays.stream(nums).sum() - minVal*(remain%2)*2;

    }
}
