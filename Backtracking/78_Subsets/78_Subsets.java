class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        backtrack(0, current, res, nums);
        return res;
    }
    private void backtrack(Integer start, List<Integer> current, List<List<Integer>> res, int[] nums) {
        if(start == nums.length) {
            res.add(new ArrayList<>(current));
            return;
        }
        
        // Include the current element
        current.add(nums[start]);
        backtrack(start+1, current, res, nums);  
        
        // Exclude the current element
        current.remove(current.size()-1);
        backtrack(start+1, current, res, nums);
    }
}
