class Solution(object):
    def sumSubarrayMins(self, arr):
        """

        907. Sum of Subarray Minimums
        Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

        

        Example 1:

        Input: arr = [3,1,2,4]
        Output: 17
        Explanation: 
        Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
        Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
        Sum is 17.
        Example 2:

        Input: arr = [11,81,94,43,3]
        Output: 444
        

        Constraints:

        1 <= arr.length <= 3 * 104
        1 <= arr[i] <= 3 * 104

        :type arr: List[int]
        :rtype: int
        """

        MOD = 10**9 + 7
        n = len(arr)
        




        # Dynamic Programming Solution        
        # This approach leverages both dynamic programming (DP) and the efficiency of a monotonic stack to compute the sum of subarray minimums in an optimal way.

        # 1. Dynamic Programming (DP): Use a DP array to store the sum of the minimums of subarrays ending at each index.
        # 2. Monotonic Stack: Use a stack to keep track of indices in a way that allows us to quickly find the previous less element for each index.
        # 3. Initialization: Create a DP array `dp` to store the sum of minimums of subarrays ending at each index.
        # 4. Initialization: Use a stack to keep track of the previous less element.
        # 5. Filling the DP Array: Iterate through the array. For each element, use the stack to find the previous less element. This helps in efficiently calculating the contribution of the current element as the minimum in some subarrays.
        # 6. Using the Stack: The stack helps maintain the indices of the elements in a way that allows us to find the previous less element quickly. If the current element is smaller than the element corresponding to the index at the top of the stack, we pop the stack.
        # 7. Calculating Contribution: For each element, calculate its contribution based on the distance to its previous less element.
        # 8. Calculating Contribution: If there is no previous less element (i.e., the stack is empty), the element contributes to all subarrays ending at its position.
        # 9. Final Sum Calculation: Sum up all values in the `dp` array to get the final result.

        # 10. Summary:
        # 11. Monotonic Stack: Efficiently finds previous less elements.
        # 12. Dynamic Programming: Uses `dp` array to store the sum of minimums of subarrays ending at each index.
        # 13. Time Complexity: O(n) due to efficient use of the stack to maintain order and find previous less elements.


        # `dp` array to store the sum of minimums ending at each index.
        dp = [0] * n

        # Use a monotonic stack to find the previous less element for each index.
        stack = []


        # a) Iterate through each element in the array.
        for i in range(n):
            # b) For each element, pop from the stack until the stack is empty or the top of the stack is less than the current element. This ensures that the stack maintains indices of elements in increasing order.
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            # c) If the stack is not empty, the top of the stack gives us the previous less element's index.
            if stack:
                prev_index = stack[-1]
                # d) Calculate the contribution of each element as the minimum in some subarrays using dynamic programming. 
                # If there is a previous less element, `dp[i]` is the sum of `dp[prev_index]` plus the contribution of the current element as the minimum in subarrays ending at `i`. 
                dp[i] = dp[prev_index] + (i - prev_index) * arr[i]
            else:
                # e) If there is no previous less element, the current element contributes to all subarrays ending at `i`.
                dp[i] = (i + 1) * arr[i]
            # f) Append the current index to the stack.
            stack.append(i)

        # Return the sum of `dp` modulo 10^9 + 7
        return sum(dp) % MOD







        # Optimized Solution Using Monotonic Stack
        
        # Use a monotonic stack to keep track of the minimum values in the subarrays.
        # We can calculate the contribution of each element as the minimum in some subarray using the previous less and next less elements.
        # The time complexity of the monotonic stack solution is \(O(n)\).


        # 1. The goal is to efficiently compute the sum of the minimum values of all subarrays. We can achieve this by understanding how each element contributes as the minimum in various subarrays.
        # 2. Previous Less Element (PLE): For each element, this is the closest element to its left that is smaller than it.
        # 3. Next Less Element (NLE): For each element, this is the closest element to its right that is smaller than it.
        # 4. prev_less[i]: The index of the previous element less than `arr[i]`. If no such element exists, it will be `-1`.
        # 5. next_less[i]: The index of the next element less than `arr[i]`. If no such element exists, it will be `n` (the length of the array).

        # Steps to Compute Contribution:
        # 6. Initialize `prev_less` to `-1` for all elements and `next_less` to `n` for all elements.
        # 7. Fill `prev_less` Array: Use a monotonic stack to determine the previous less element for each index.
        # 8. *Fill `next_less` Array: Use a monotonic stack to determine the next less element for each index.
        # 9. For each element, compute its contribution to the sum of subarray minimums using the `prev_less` and `next_less` arrays.
        # 9bis. The number of subarrays where `arr[i]` is the minimum can be determined by the distances to its previous and next less elements. Specifically, `arr[i]` contributes as the minimum in `(i - prev_less[i]) * (next_less[i] - i)` subarrays.

        # 10 Summary: `prev_less[i]` and `next_less[i]` store indices of the previous and next smaller elements.        
        # 11. These arrays help determine how many subarrays include `arr[i]` as their minimum.
        # 12. The contribution of each element is calculated based on the distances to these previous and next less elements.
        # 13. The use of monotonic stacks ensures efficient O(n) computation for large arrays.



        # Use a monotonic stack to find the previous less element for each index.
        # For each element `arr[i]`, we use the stack to find the nearest smaller element to its left. If the stack is not empty, the top of the stack will be the previous less element for `arr[i]`.
        prev_less = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                prev_less[stack.pop()] = i
            stack.append(i)


        # Use a monotonic stack to find the next less element for each index.
        # For each element `arr[i]`, we use the stack to find the nearest smaller element to its right. If the stack is not empty, the top of the stack will be the next less element for `arr[i]`.
        next_less = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_less[stack.pop()] = i
            stack.append(i)



        res = 0

        # Calculate the contribution of each element as the minimum in some subarrays.
        # For each element `arr[i]`, calculate its contribution. 
        # The number of subarrays where `arr[i]` is the minimum can be determined by the distances to its previous and next less elements. Specifically, `arr[i]` contributes as the minimum in `(i - prev_less[i]) * (next_less[i] - i)` subarrays.
        
        for i in range(n):
           res += arr[i] * (i - prev_less[i]) * (next_less[i] - i)
           res %= MOD

        return res       




        ### Brute Force Solution
        
        # The brute force solution involves generating all possible subarrays and calculating the sum of their minimum values
        # The time complexity of the brute force solution is O(n^3), which is very high for large arrays.
        
        # MOD = 10**9 + 7
        
        # res = 0
        # n = len(arr)

        # # Check all subarrays
        # for i in range(n):
        #    for j in range(i, n):
        #        res += min(arr[i:j+1])

        # return res % MOD