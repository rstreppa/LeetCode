class Solution {
public:
    string decodeAtIndex(string s, int k) {
        long long size = 0; // Use long long to handle larger sizes
        size_t n = s.length();

        // First pass: find the size of the decoded string
        for (size_t i = 0; i < n; ++i) {
            if (isdigit(s[i])) {
                size *= (s[i] - '0'); // Correct conversion from char to int
            } else {
                size++;
            }
        }

        // Second pass: backtrack to find the kth character
        for (size_t i = n; i-- > 0;) { // Updated loop to avoid size_t underflow
            k %= size; // k should be modulo size every time to keep it in bounds
            if (k == 0 && isalpha(s[i])) {
                return string(1, s[i]); // Return a string containing the character
            }

            if (isdigit(s[i])) {
                size /= (s[i] - '0'); // Correct division by the integer value of the digit
            } else {
                size--;
            }
        }

        // This point should not be reached if the input is valid
        return "";
    }
};
