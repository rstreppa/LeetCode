class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        
        // Adjusted adjacency list to hold vectors of pairs
        unordered_map<int, vector<pair<int, double>>> adj;

        // Populate the adjacency list
        for(size_t i = 0; i < edges.size(); i++) {
            int src = edges[i][0];
            int dst = edges[i][1];
            adj[src].emplace_back(dst, succProb[i]);
            adj[dst].emplace_back(src, succProb[i]); // Assuming it's an undirected graph
        }

        // Priority queue to process nodes by highest probability
        priority_queue<pair<double, int>> pq;
        pq.push({1.0, start_node}); // start with probability 1.0 at the start node

        // Vector to store the maximum probability to reach each node
        vector<double> maxProb(n, 0.0);
        maxProb[start_node] = 1.0;

        while(!pq.empty()) {
            auto [prob, curr] = pq.top();
            pq.pop();

            if (curr == end_node) {
                return prob;  // Return the probability when reaching the end node
            }

            for (auto& [nei, edgeProb] : adj[curr]) {
                double newProb = prob * edgeProb;

                if (newProb > maxProb[nei]) {  // Only consider this path if it provides a higher probability
                    maxProb[nei] = newProb;
                    pq.push({newProb, nei});
                }
            }
        }

        return 0.0; // If there's no path found
    }

};