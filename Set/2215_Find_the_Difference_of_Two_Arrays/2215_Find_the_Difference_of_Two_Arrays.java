class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        
        List<List<Integer>> answer = new ArrayList<List<Integer>>();

        Set<Integer> h1 = new HashSet<Integer>();
        for(int elem: nums1)
            h1.add(elem);
        
        Set<Integer> h2 = new HashSet<Integer>();
        for(int elem: nums2)
            h2.add(elem);

        Set<Integer> temp = new HashSet<>(h1);

        h1.removeAll(h2);
        h2.removeAll(temp);

        List<Integer> v1 = new ArrayList<>(h1);
        List<Integer> v2 = new ArrayList<>(h2);

        answer.add(v1);
        answer.add(v2);

        return answer;

    }
}