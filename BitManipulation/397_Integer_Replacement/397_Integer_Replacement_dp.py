class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        397. Integer Replacement
        Medium
        Given a positive integer n, you can apply one of the following operations:

        If n is even, replace n with n / 2.
        If n is odd, replace n with either n + 1 or n - 1.
        Return the minimum number of operations needed for n to become 1.

        Example 1:
        Input: n = 8
        Output: 3
        Explanation: 8 -> 4 -> 2 -> 1

        Example 2:
        Input: n = 7
        Output: 4
        Explanation: 7 -> 8 -> 4 -> 2 -> 1
        or 7 -> 6 -> 3 -> 2 -> 1

        Example 3:
        Input: n = 4
        Output: 2
        """
        dp = {1: 0, 2: 1}  # base cases

        def helper(num):
            if num not in dp:
                if num % 2 == 0:
                    dp[num] = 1 + helper(num // 2)
                else:
                    dp[num] = 1 + min(helper(num + 1), helper(num - 1))
            return dp[num]

        return helper(n)
