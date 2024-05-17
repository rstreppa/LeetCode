class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> d = new HashMap<>();
        for(int i=0; i<nums.length; i++) {
            if(d.containsKey(nums[i]) && Math.abs(i-d.get(nums[i])) <=k)
                return true;
            d.put(nums[i], i);
        }

        return false;
    }
}