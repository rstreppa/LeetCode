class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool


        383. Ransom Note

        Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

        Each letter in magazine can only be used once in ransomNote.

        

        Example 1:

        Input: ransomNote = "a", magazine = "b"
        Output: false
        Example 2:

        Input: ransomNote = "aa", magazine = "ab"
        Output: false
        Example 3:

        Input: ransomNote = "aa", magazine = "aab"
        Output: true
        

        Constraints:

        1 <= ransomNote.length, magazine.length <= 105
        ransomNote and magazine consist of lowercase English letters.

        """
        r = {}
        m = {}
        for c in ransomNote:
            r[c] = r.get(c, 0) + 1   

        for c in magazine:
            m[c] = m.get(c, 0) + 1   

        for key, val in r.items():
            if key not in m:
                return False
            if m[key] < r[key]:
                return False

        return True
