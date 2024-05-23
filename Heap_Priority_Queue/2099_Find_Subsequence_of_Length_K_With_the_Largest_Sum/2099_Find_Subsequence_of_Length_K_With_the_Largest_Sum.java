class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        
        // Create a list of indexed values
        List<Pair<Integer, Integer>> indexedNums = new ArrayList<>();
        for (int i = 0; i < nums.length; ++i) {
            indexedNums.add(new Pair<>(nums[i], i));
        }

        // Use a max heap to find the k largest elements based on their values
        PriorityQueue<Pair<Integer, Integer>> maxHeap = new PriorityQueue<>((a, b) -> {
            if (!a.getKey().equals(b.getKey())) {
                return a.getKey() - b.getKey(); // Compare by values in descending order
            } else {
                return b.getValue() - a.getValue(); // If values are equal, compare by indices in descending order
            }
        });

        for (Pair<Integer, Integer> pair : indexedNums) {
            maxHeap.add(pair);
            if (maxHeap.size() > k) {
                maxHeap.poll();
            }
        }


        // Extract the k largest elements and sort them by their original indices
        List<Pair<Integer, Integer>> largestKElements = new ArrayList<>();
        while (!maxHeap.isEmpty()) {
            largestKElements.add(maxHeap.poll());
        }

        // Sort based on original indices to maintain order
        Collections.sort(largestKElements, Comparator.comparingInt(Pair::getValue));

        // Extract the values of the sorted k largest elements
        int[] result = new int[k];
        for (int i = 0; i < k; ++i) {
            result[i] = largestKElements.get(i).getKey();
        }

        return result;

    }
}