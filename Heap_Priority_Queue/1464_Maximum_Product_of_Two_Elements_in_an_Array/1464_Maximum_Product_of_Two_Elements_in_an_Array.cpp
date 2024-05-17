class Solution {
public:
    int maxProduct(vector<int>& nums) {

        // 1. Use a max-heap (priority queue) to keep track of largest and second largest elements
        // 2. Pop the two largest elements and return desired product 

        priority_queue<int> max_heap;

        for(auto& num : nums)
            max_heap.push(num);

        // pop the two largest elements
        int max1 = max_heap.top();
        max_heap.pop();
        int max2 = max_heap.top();

        return (max1-1)*(max2-1);

    }
};