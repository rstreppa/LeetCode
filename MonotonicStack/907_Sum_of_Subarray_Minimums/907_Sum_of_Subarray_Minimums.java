class Solution {
    public int sumSubarrayMins(int[] arr) {

        final int MOD = 1000000007;
        int n = arr.length;

        List<Long> dp = new ArrayList<>(Collections.nCopies(n, 0L));
        Stack<Integer> stack = new Stack<>();        
    
        for(int i = 0; i<n; i++) {
            while(!stack.isEmpty() && arr[stack.peek()] > arr[i]) 
                stack.pop();
            if(!stack.isEmpty()) {
                int prev_index = stack.peek();        
                dp.set(i, (dp.get(prev_index) + (i - prev_index) * (long)arr[i]) % MOD);
            }
            else
                dp.set(i, ((i + 1) * (long)arr[i]) % MOD);
            stack.push(i);    
        }
        long res = 0;
        for(long v : dp) 
            res = (res+v) % MOD;
        return (int)res;
    }
}