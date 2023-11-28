class Solution {

    private Map<Integer, Set<Integer>> map;
    private Random random;


    public Solution(int[] nums) {
        map = new HashMap<>();
        random = new Random();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i], new HashSet<>());
            }
            map.get(nums[i]).add(i);
        } 
    }
    
    public int pick(int target) {
        Set<Integer> indices = map.get(target);
        int randomIndex = random.nextInt(indices.size());
        int idx = 0;
        for (Integer index : indices) {
            if (idx == randomIndex) {
                return index;
            }
            idx++;
        }
        return -1;  // This should never happen if the target exists in the map.        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */