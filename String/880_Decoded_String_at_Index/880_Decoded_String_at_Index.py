class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str

        880. Decoded String at Index
        Medium
        You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time 
        and the following steps are taken:

        If the character read is a letter, that letter is written onto the tape.
        If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
        Given an integer k, return the kth letter (1-indexed) in the decoded string.

        Example 1:
        Input: s = "leet2code3", k = 10
        Output: "o"
        Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
        The 10th letter in the string is "o".
        
        Example 2:
        Input: s = "ha22", k = 5
        Output: "h"
        Explanation: The decoded string is "hahahaha".
        The 5th letter is "h".
        
        Example 3:
        Input: s = "a2345678999999999999999", k = 1
        Output: "a"
        Explanation: The decoded string is "a" repeated 8301530446056247680 times.
        The 1st letter is "a".
        """
        
        # Naive solution creating a buffer to store the decoded string: The given solution is close to the right approach 
        # but has a   few issues in handling the buffer expansion and digit characters. Specifically, it does not correctly handle
        # the size of the string after each digit character. When encountering a digit, the total length of the string increases 
        # by a factor of that digit, which can exponentially increase the length and cause inefficiencies. 
        # Moreover, directly appending to buffer can lead to memory issues for large strings.

        # To fix this, instead of actually building the string, you can calculate the size of the string after each step 
        # and then backtrack to find the character corresponding to index k.

        size = 0
        n = len(s)

        # First pass: find the size of the decoded string
        for i in range(n):
            if s[i].isdigit():
                size *= int(s[i])
            else:
                size += 1

        # Second pass: backtrack to find the kth character
        # 1. Iterating Backwards: The second pass iterates through the string s in reverse order, from the last character to the first. The reason for going backwards is that we are effectively "unwrapping" the encoded string. We start from the end because the expansion caused by the digits in the string happens in a forward direction, so to reverse the process, we go backward.

        # 2. Modulo Operation (k %= size): This line is key to understanding the backtracking process. The modulo operation here is used to keep track of the 'effective' position of k in the original unexpanded string. As we reverse the process of expanding the string, k is updated to reflect its position in the progressively smaller string.

        # 3. Checking for the Character:
        #   * If k becomes 0 and the current character is an alphabet letter, it means k points to this letter in the decoded string, and we return this character.
        #   * The condition k == 0 is necessary because, after modulo operation, k might become 0, indicating that the target character is at the current position.
        # 4. Handling Digits and Letters:
        #   * If the current character is a digit (say d), the line size //= int(s[i]) reduces the size of the decoded string to what it was before this digit was encountered. This is because each digit multiplies the size of the string by its value. So, to reverse this, we divide the size by the digit.
        #   * If the current character is a letter, size -= 1 simply reduces the size by one, reversing the addition of a single character to the string in the forward direction.
        # By the end of this loop, if we haven't returned a character, it would mean that the input was invalid or k was out of bounds for the decoded string (which should not happen with valid input according to the problem's constraints).        

        for i in reversed(range(n)):
            k %= size
            if k == 0 and s[i].isalpha():
                return s[i]

            if s[i].isdigit():
                size //= int(s[i])
            else:
                size -= 1

        # This point should not be reached if the input is valid
        return None
        