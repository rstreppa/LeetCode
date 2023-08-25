class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        if (n == 0) {
            return 0;
        }
        
        int res = 1;  // Initialize the result to 1 since a single character substring is always valid
        unordered_map<char, int> d;  // To store the occurrences of characters in the current window
        int i = 0, j = 0;  // Pointers to the start and end of the current substring
        
        while (j < n) 
        {
            if (d.find(s[j]) == d.end() || d[s[j]] == 0) {  // Character is not in the current window
                d[s[j]] = 1;
                res = max(res, j - i + 1);
                j++;
            } else {  // Character is in the current window
                d[s[i]] -= 1;  // Decrease the frequency of the character at the start of the window
                i++;  // Move the start of the window to the right
            }
        }
        return res;    
    }
};
