class Solution {
    public int maximizeSum(int[] nums, int k) {


        int m = Arrays.stream(nums).max().getAsInt();

        return k*m + k*(k-1)/2; 

    }
}