class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        backtrack(0, current, res, nums);
        return res;
    }
    
    private void backtrack(int start, List<Integer> current, List<List<Integer>> res, int[] nums) {
        res.add(new ArrayList<>(current));
        for(int i = start; i < nums.length; i++) {
            if(i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            current.add(nums[i]);
            backtrack(i + 1, current, res, nums);
            current.remove(current.size() - 1);
        }
    }
}
