class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # TC O(n^2) SP O(n^2), Dynamic Programming solution

        n = len(s)
        if n == 0:
            return ""
        
        # Initialize a DP table
        dp = [[False] * n for _ in range(n)]
        
        start = 0  # The starting index of the longest palindromic substring found so far
        max_length = 1  # The length of the longest palindromic substring found so far
        
        # Every individual character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # Check for a palindrome of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
                
        # Check for lengths greater than 2. k is length of palindrome
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1  # Ending index of current palindrome substring
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
                        
        return s[start:start + max_length]
    
