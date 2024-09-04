class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        // Adjacency list: each node maps to a list of pairs (neighbor, edge probability)
        Map<Integer, List<Pair<Integer, Double>>> adj = new HashMap<>();

        // Build the graph
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            double prob = succProb[i];

            adj.computeIfAbsent(u, k -> new ArrayList<>()).add(new Pair<>(v, prob));
            adj.computeIfAbsent(v, k -> new ArrayList<>()).add(new Pair<>(u, prob));
        }

        // Priority queue for Dijkstra's algorithm (max-heap based on probability)
        PriorityQueue<Pair<Double, Integer>> pq = new PriorityQueue<>((a, b) -> Double.compare(b.getKey(), a.getKey()));
        pq.offer(new Pair<>(1.0, start));

        // Array to store the max probability to reach each node
        double[] maxProb = new double[n];
        maxProb[start] = 1.0;

        // Dijkstra's algorithm
        while (!pq.isEmpty()) {
            Pair<Double, Integer> current = pq.poll();
            double prob = current.getKey();
            int node = current.getValue();

            if (node == end) return prob; // Early exit if end node is reached

            // Iterate over neighbors
            for (Pair<Integer, Double> neighbor : adj.getOrDefault(node, new ArrayList<>())) {
                int nextNode = neighbor.getKey();
                double edgeProb = neighbor.getValue();
                double newProb = prob * edgeProb;

                if (newProb > maxProb[nextNode]) {
                    maxProb[nextNode] = newProb;
                    pq.offer(new Pair<>(newProb, nextNode));
                }
            }
        }

        return 0.0; // If no path exists
    }

    // Pair class to hold node and probability
    class Pair<K, V> {
        private K key;
        private V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }
}