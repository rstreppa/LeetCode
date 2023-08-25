class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        3. Longest Substring Without Repeating Characters
        Medium
        Given a string s, find the length of the longest substring without repeating characters.
              
        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        
        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        
        Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
                
        """

        # Sliding Window: you should only increment i and decrement the count of the character at index i in the dictionary when a duplicate character is found. 
        # You should not move j forward in this case.
      
        n = len(s)
        if n == 0:
            return 0
        res = 1
        d   = {}
        i   = 0
        j   = 0
        while j < n:
            if s[j] not in d or d[s[j]] == 0:
                d[s[j]] = 1
                res = max(res, j - i + 1)
                j += 1
            else:
                d[s[i]] -= 1
                i += 1
        return res
