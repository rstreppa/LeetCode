import java.util.HashMap;

public class Solution {
    public boolean isPossible(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<>();  // To hold the count of each number in nums
        HashMap<Integer, Integer> tails = new HashMap<>();  // To hold the count of subsequences ending with each number
        
        // Populate count with the frequency of each number in nums
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Iterate through nums to populate tails
        for (int num : nums) {
            if (count.get(num) == 0) {
                continue;  // Skip if this number is already used
            }

            // Decrease the count for this number, since we're using one instance of it
            count.put(num, count.get(num) - 1);
            
            // Try to add num to an existing subsequence
            if (tails.getOrDefault(num - 1, 0) > 0) {
                tails.put(num - 1, tails.get(num - 1) - 1);  // Remove one subsequence ending with num - 1
                tails.put(num, tails.getOrDefault(num, 0) + 1);  // Add a new subsequence ending with num
            }
            // Else start a new subsequence if possible
            else if (count.getOrDefault(num + 1, 0) > 0 && count.getOrDefault(num + 2, 0) > 0) {
                count.put(num + 1, count.get(num + 1) - 1);
                count.put(num + 2, count.get(num + 2) - 1);
                tails.put(num + 2, tails.getOrDefault(num + 2, 0) + 1);
            }
            // Else cannot form a valid subsequence
            else {
                return false;
            }
        }
        
        return true;
    }
}
