class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        const int MOD = 1000000007;
        
        size_t n = arr.size();

        vector<long long> dp(n, 0);
        stack<size_t> stack;

        for(size_t i = 0; i<n; i++) {
            while(!stack.empty() && arr[stack.top()] > arr[i]) 
                stack.pop();
            if(!stack.empty()) {
                size_t prev_index = stack.top();        
                dp[i] = (dp[prev_index] + (i - prev_index) * (long long)arr[i]) % MOD;
            }
            else
                dp[i] = ((i + 1) * (long long)arr[i]) % MOD;
            stack.push(i);    
        }
        return accumulate(dp.begin(),dp.end(),0LL) % MOD;
    }
};