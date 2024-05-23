class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {

		// Priority Queue

        // More efficient: use a max heap to keep track of the indices of the k largest elements, then extract them while preserving original order
        // Using the priority queue to have a complexity of O(n log k)

        // Create a list of indexed values
        vector<pair<int, int>> indexed_nums;
        for (int i = 0; i < nums.size(); ++i) {
            indexed_nums.push_back({nums[i], i});
        }
 

        // Use a max heap to find the k largest elements
        auto comp = [](pair<int, int>& a, pair<int, int>& b) {
            return a.first > b.first; // max heap based on value
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> max_heap(comp);

        for (auto& p : indexed_nums) {
            max_heap.push(p);
            if (max_heap.size() > k) {
                max_heap.pop();
            }
        }

        // Extract the k largest elements and sort them by their original indices
        vector<pair<int, int>> largest_k_elements;
        while (!max_heap.empty()) {
            largest_k_elements.push_back(max_heap.top());
            max_heap.pop();
        }

        // Sort based on original indices to maintain order
        sort(largest_k_elements.begin(), largest_k_elements.end(), [](pair<int, int>& a, pair<int, int>& b) {
            return a.second < b.second;
        });

        // Extract the values of the sorted k largest elements
        vector<int> res;
        for (auto& p : largest_k_elements) {
            res.push_back(p.first);
        }

        return res;









    }
};