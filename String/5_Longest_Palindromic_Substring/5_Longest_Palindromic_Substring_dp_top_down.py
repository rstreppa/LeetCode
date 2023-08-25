class Solution:

    # Python DP top down
    # Time limit exceeded due to recursion
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
       
        # Initialize a memoization table
        memo = {}
       
        def dp(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
           
            # Base cases
            if l > r:
                return ""
            if l == r:
                return s[l]
           
            # Check for palindrome
            if s[l] == s[r]:
                if r - l == 1:
                    memo[(l, r)] = s[l:r+1]
                else:
                    inner_palindrome = dp(l+1, r-1)
                    if len(inner_palindrome) == r - l - 1:
                        memo[(l, r)] = s[l] + inner_palindrome + s[r]
                    else:
                        left_palindrome = dp(l, r-1)
                        right_palindrome = dp(l+1, r)
                        memo[(l, r)] = left_palindrome if len(left_palindrome) > len(right_palindrome) else right_palindrome
            else:
                left_palindrome = dp(l, r-1)
                right_palindrome = dp(l+1, r)
                memo[(l, r)] = left_palindrome if len(left_palindrome) > len(right_palindrome) else right_palindrome
               
            return memo[(l, r)]
       
        return dp(0, n-1)
