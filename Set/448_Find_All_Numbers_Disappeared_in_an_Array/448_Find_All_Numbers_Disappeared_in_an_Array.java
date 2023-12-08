class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        List<Integer> res = new ArrayList<>();
        int n = nums.length;

        for (int num : nums) {
            numSet.add(num);
        }

        for (int i = 1; i <= n; i++) {
            if (!numSet.contains(i)) {
                res.add(i);
            }
        }
        return res;        
    }
}