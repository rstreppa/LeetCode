class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int

        1160. Find Words That Can Be Formed by Characters
        Solved
        Easy
        You are given an array of strings words and a string chars.
        A string is good if it can be formed by characters from chars (each character can only be used once).
        Return the sum of lengths of all good strings in words.

        Example 1:
        Input: words = ["cat","bt","hat","tree"], chars = "atach"
        Output: 6
        Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
        
        Example 2:
        Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
        Output: 10
        Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
        """
        d = {}
        for c in chars:
            d[c] = d.get(c, 0) + 1
    
        def check(word, chars, d):
            if len(word) > len(chars):
                return False
            temp = {}
            for c in word:
                temp[c] = temp.get(c, 0) + 1
                if c not in d.keys() or d[c] < temp[c]:
                    return False
            return True

        return sum(len(word) for word in words if check(word, chars, d))       
        