import java.util.HashMap;
import java.util.Collections;
import java.util.ArrayList;

public class Solution {
    public int largestUniqueNumber(int[] A) {
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num : A) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        ArrayList<Integer> uniqueNums = new ArrayList<>();
        for (int key : countMap.keySet()) {
            if (countMap.get(key) == 1) {
                uniqueNums.add(key);
            }
        }

        if (uniqueNums.isEmpty()) {
            return -1;
        }

        Collections.sort(uniqueNums);
        return uniqueNums.get(uniqueNums.size() - 1);
    }
}
