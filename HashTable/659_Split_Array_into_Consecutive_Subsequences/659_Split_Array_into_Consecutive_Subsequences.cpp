#include <unordered_map>
#include <vector>

class Solution {
public:
    bool isPossible(std::vector<int>& nums) {
        std::unordered_map<int, int> count;  // To hold the count of each number in nums
        std::unordered_map<int, int> tails;  // To hold the count of subsequences ending with each number
        
        // Populate count with the frequency of each number in nums
        for (int num : nums) {
            ++count[num];
        }

        // Iterate through nums to populate tails
        for (int num : nums) {
            if (count[num] == 0) {
                continue;  // Skip if this number is already used
            }

            // Decrease the count for this number, since we're using one instance of it
            --count[num];
            
            // Try to add num to an existing subsequence
            if (tails[num - 1] > 0) {
                --tails[num - 1];  // Remove one subsequence ending with num - 1
                ++tails[num];  // Add a new subsequence ending with num
            }
            // Else start a new subsequence if possible
            else if (count[num + 1] > 0 && count[num + 2] > 0) {
                --count[num + 1];
                --count[num + 2];
                ++tails[num + 2];
            }
            // Else cannot form a valid subsequence
            else {
                return false;
            }
        }
        
        return true;
    }
};