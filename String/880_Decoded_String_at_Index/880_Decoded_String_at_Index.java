class Solution {
    public String decodeAtIndex(String s, int k) {
        long size = 0; // Use long long to handle larger sizes
        int n = s.length();

        // First pass: find the size of the decoded string
        for (int i = 0; i < n; ++i) {
            if (Character.isDigit(s.charAt(i))) {
                size *= (s.charAt(i) - '0'); // Correct conversion from char to int
            } else {
                size++;
            }
        }

        // Second pass: backtrack to find the kth character
        for (int i = n; i-- > 0;) { // Updated loop to avoid size_t underflow
            k %= size; // k should be modulo size every time to keep it in bounds
            if (k == 0 && Character.isLetter(s.charAt(i))) {
                return Character.toString(s.charAt(i)); // Return a string containing the character
            }

            if (Character.isDigit(s.charAt(i))) {
                size /= (s.charAt(i) - '0'); // Correct division by the integer value of the digit
            } else {
                size--;
            }
        }

        // This point should not be reached if the input is valid
        return "";            
    }
}