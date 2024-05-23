# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        316. Remove Duplicate Letters
        Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
        the smallest in lexicographical order
        among all possible results.

        

        Example 1:

        Input: s = "bcabc"
        Output: "abc"
        Example 2:

        Input: s = "cbacdcbc"
        Output: "acdb"
        

        Constraints:

        1 <= s.length <= 104
        s consists of lowercase English letters.
 
        :type s: str
        :rtype: str
        """

        # Monotonic stack approach

        # 1. Count Array: Keep track of the remaining count of each character. Track how many times each character appears in the string.   
        # 2. Stack and In-Stack set: Use a stack to build the result and a set to check for duplicates in the stack.
        # 3. Iteration and Conditions:
        #   3a. Decrement the count for the current character.
        #   3b. Skip the character if it's already in the stack.
        #   3c. While the current character is smaller than the last character in the stack and the last character appears later in the string, remove the last character from the stack.
        #   3d. Add the current character to the stack and mark it as in the stack.
        # 4. Build Result: Join the stack into a string to get the final result.

        # The overall time complexity is O(n), where n is the length of the input string, making this approach optimal for large strings.


        # 1. Count the frequency of each character
        count = {c: 0 for c in s}
        for c in s:
            count[c] += 1

        # 2. Initialize the stack and a set to keep track of characters in the stack
        stack = []
        in_stack = set()

        # 3. Iterate over each character in the string
        for c in s:
            count[c] -= 1  # 3a. Decrease the count for the current character

            if c in in_stack:
                continue  # 3b. Skip if the character is already in the stack

            # 3c. Maintain the stack in lexicographical order
            while stack and c < stack[-1] and count[stack[-1]] > 0:
                in_stack.remove(stack.pop())

            # 3d. Add the current character to the stack and the set
            stack.append(c)
            in_stack.add(c)

        # 4. Build and return the result string from the stack
        return ''.join(stack)
