import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        HashSet<Integer> visited = new HashSet<>();
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (!visited.contains(i)) {
                bfs(i, visited, isConnected, n);
                res++;
            }
        }
        return res;       
    }
    private void bfs(int i, HashSet<Integer> visited, int[][] isConnected, int n) {
        Queue<Integer> q = new LinkedList<>();
        q.add(i);
        while (!q.isEmpty()) {
            int curr = q.poll();
            visited.add(curr);
            for (int j = 0; j < n; j++) {
                if (isConnected[curr][j] == 1 && !visited.contains(j)) {
                    q.add(j);
                    visited.add(j);
                }
            }
        }
    }
}