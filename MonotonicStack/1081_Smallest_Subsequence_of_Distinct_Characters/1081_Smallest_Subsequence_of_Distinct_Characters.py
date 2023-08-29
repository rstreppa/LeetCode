class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        1081. Smallest Subsequence of Distinct Characters
        Medium
        Given a string s, return the lexicographically smallest subsequence
        of s that contains all the distinct characters of s exactly once.

        Example 1:
        Input: s = "bcabc"
        Output: "abc"

        Example 2:
        Input: s = "cbacdcbc"
        Output: "acdb"
        """

        # first use a hash to count characters with number of occurrences
        # then use a mono stack to put chars in ascending order as much as you can
        # you cannot do completetely, else you would simply
        # do a sort on ther set of chars
        
        hash = {}
        for c in s:
            hash[c] = hash.get(c, 0) + 1

        stack = []

        for c in s:
            hash[c] -= 1    # Decrement the count as we are using this character now
            if c in stack:  # Skip if the character is already in the result stack
                continue

            # Check stack is not empty and conditions for pop
            while stack and c < stack[-1] and hash[stack[-1]] > 0:
                stack.pop()

            stack.append(c)
        
        return "".join(stack)
