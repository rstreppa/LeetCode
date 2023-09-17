import java.util.*;

class Solution {
    public int numIslands(char[][] grid) {

         if (grid.length < 1 || grid[0].length < 1) {
            return 0; //empty
        }
        
        int res = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        Set<Map.Entry<Integer, Integer>> visited = new HashSet<>();
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                Map.Entry<Integer, Integer> pair = new AbstractMap.SimpleEntry<>(r, c);
                if (grid[r][c] == '1' && !visited.contains(pair)) {
                    bfs(r, c, grid, visited, rows, cols);
                    res++;
                }
            }
        }
        return res;    
    }
    private void bfs(int r, int c, char[][] grid, Set<Map.Entry<Integer, Integer>> visited, int rows, int cols) {
        List<Map.Entry<Integer, Integer>> directions = Arrays.asList(
            new AbstractMap.SimpleEntry<>(1, 0),
            new AbstractMap.SimpleEntry<>(-1, 0),
            new AbstractMap.SimpleEntry<>(0, 1),
            new AbstractMap.SimpleEntry<>(0, -1)
        );
        
        Queue<Map.Entry<Integer, Integer>> q = new LinkedList<>();
        visited.add(new AbstractMap.SimpleEntry<>(r, c));
        q.add(new AbstractMap.SimpleEntry<>(r, c));
        
        while (!q.isEmpty()) {
            Map.Entry<Integer, Integer> curr = q.poll();
            int row = curr.getKey();
            int col = curr.getValue();
            for (Map.Entry<Integer, Integer> p : directions) {
                int dr = p.getKey();
                int dc = p.getValue();
                int curr_r = row + dr;
                int curr_c = col + dc;
                Map.Entry<Integer, Integer> pair = new AbstractMap.SimpleEntry<>(curr_r, curr_c);
                if (curr_r >= 0 && curr_r < rows && curr_c >= 0 && curr_c < cols && grid[curr_r][curr_c] == '1' && !visited.contains(pair)) {
                    q.add(pair);
                    visited.add(pair);
                }
            }
        }
    }
}