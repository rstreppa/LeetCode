class Solution {
public:
    string longestPalindrome(string s) {
        // Helper lambda function to expand from the middle and find palindrome length
        auto expandFromMiddle = [&](int left, int right) -> int {
            if (s.empty() || left > right) return 0;
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                --left;
                ++right;
            }
            return right - left - 1;
        };

        if (s.empty() || s.length() < 1) return "";

        int start = 0, end = 0;
        for (int i = 0; i < s.length(); ++i) {
            int len1 = expandFromMiddle(i, i);
            int len2 = expandFromMiddle(i, i + 1);
            int maxlen = max(len1, len2);
            if (maxlen > end - start) {
                start = i - (maxlen - 1) / 2;
                end = i + maxlen / 2;
            }
        }
        return s.substr(start, end - start + 1);        
    }
}
