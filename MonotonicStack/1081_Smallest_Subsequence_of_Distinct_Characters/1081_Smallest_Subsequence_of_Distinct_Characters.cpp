class Solution {
public:
    string smallestSubsequence(string s) {
        // Using unordered_map as a substitute for Python's dict
        std::unordered_map<char, int> hash;

        // Populating the hash map
        for (char c : s) {
            hash[c] = hash.find(c) != hash.end() ? hash[c] + 1 : 1;
        }

        // Using vector as a substitute for Python's list (acting as a stack)
        std::vector<char> stack;

        for (char c : s) {
            hash[c]--; // Decrement the count as we are using this character now

            // Skip if the character is already in the result stack
            if (std::find(stack.begin(), stack.end(), c) != stack.end()) {
                continue;
            }

            // Check stack is not empty and conditions for pop
            while (!stack.empty() && c < stack.back() && hash[stack.back()] > 0) {
                stack.pop_back();
            }

            stack.push_back(c);
        }

        // Converting the vector to a string
        return std::string(stack.begin(), stack.end());        
    }
};
