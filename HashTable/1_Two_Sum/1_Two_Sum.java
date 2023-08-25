class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        res[0]  = -1;
        res[1]  = -1;
        HashMap<Integer, Integer> hash = new HashMap<>();
        for( int i=0; i<nums.length; ++i )
        {
            if( hash.containsKey(target-nums[i]) )
            {
                res[0] = i;
                res[1] = hash.get(target-nums[i]);       
            }
            else
            {
                hash.put( nums[i], i );
            }
        }
        return res;
    }
}
