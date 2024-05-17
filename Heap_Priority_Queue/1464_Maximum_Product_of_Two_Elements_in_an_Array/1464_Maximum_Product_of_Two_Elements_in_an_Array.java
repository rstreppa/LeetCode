class Solution {
    public int maxProduct(int[] nums) {

        // 1. Use a max-heap (priority queue) to keep track of largest and second largest elements
        // 2. Pop the two largest elements and return desired product 

        // Use a max heap: negate the values to simulate a max heap
        PriorityQueue<Integer> max_heap = new PriorityQueue<>(nums.length, Collections.reverseOrder());

        for(Integer num : nums)
            max_heap.add(num);

        // pop the two largest elements
        Integer max1 = max_heap.poll();
        Integer max2 = max_heap.poll();

        return (max1-1)*(max2-1);
        
    }
}


