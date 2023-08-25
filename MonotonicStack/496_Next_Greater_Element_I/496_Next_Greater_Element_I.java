class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stk = new Stack<>();
        stk.push(Integer.MAX_VALUE);
        HashMap<Integer,Integer> hash = new HashMap<>();
        List<Integer> res = new ArrayList<>();

        for( int num: nums2 ){
            while( num > stk.peek() ) {
                Integer key = stk.pop();
                hash.put(key, num);
            }
            stk.push(num);
        }  
        
        for( int num: nums1 ){
            if(hash.containsKey(num)) {
                res.add(hash.get(num));
            } else {
                res.add(-1);
            }
        }
        int[] result = new int[res.size()];
        int i = 0;
        for (Integer num : res) {
            result[i++] = num;
        }
        return result;
    }
}
