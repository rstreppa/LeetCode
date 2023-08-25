class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        5. Longest Palindromic Substring
        Medium
        Given a string s, return the longest palindromic substring in s.
              
        Example 1:
        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.
        
        Example 2:
        Input: s = "cbbd"
        Output: "bb"
        
        """
        # https://www.youtube.com/watch?v=y2BD4MJqV20
        # TC O(n^2) SP O(1), beats Dynamic Programming

        def expandFromMiddle( s, left, right ):
            if not s or left > right:
                return 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left  -= 1
                right += 1
            return right - left - 1


        if not s or len(s) < 1:
            return ""

        start = 0
        end   = 0
        for i in range(len(s)):
            len1   = expandFromMiddle( s, i, i )
            len2   = expandFromMiddle( s, i, i+1 )
            maxlen = max( len1, len2 )
            if maxlen > end - start:
                start = i - (maxlen-1)//2
                end   = i + maxlen//2 
        
        return s[start:end+1]
