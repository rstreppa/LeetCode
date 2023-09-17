class Solution {
public:
    int numIslands(vector<vector<char>>& grid) 
    {
        if(grid.empty())
            return 0; 
        
        int res = 0;
        size_t rows = grid.size();
        size_t cols = grid[0].size();
        set<pair<size_t, size_t>> visited;

        for(size_t r = 0; r < rows; r++) {
            for(size_t c = 0; c < cols; c++) {
                auto pos = visited.find(make_pair(r,c));
                if(grid[r][c] == '1' && pos == visited.end()) {
                    bfs(r, c, grid, visited, rows, cols);
                    res++;
                }
            }
        }
        return res;    
    }
private:
    // do not pass visited by value, which means that changes to visited inside bfs will not be reflected outside the function. 
    // You should pass it by reference instead.
    void bfs(size_t r, size_t c, vector<vector<char>>& grid, set<pair<size_t, size_t>>& visited, size_t rows, size_t cols) 
    {
        vector<pair<int, int>> directions {{1, 0},{-1, 0},{0, 1},{0, -1}};
        queue<pair<size_t, size_t>> q;
        visited.insert(make_pair(r,c));
        q.push(make_pair(r,c));
        
        while(!q.empty()) {
            pair<size_t, size_t> curr = q.front(); q.pop();
            size_t row = curr.first;
            size_t col = curr.second;
            for(auto p : directions) {
                int dr = p.first;
                int dc = p.second;
                size_t curr_r = row + dr;
                size_t curr_c = col + dc;
                auto pos = visited.find(make_pair(curr_r,curr_c));
                if(curr_r < rows && curr_c < cols && grid[curr_r][curr_c] == '1' && pos == visited.end()) {
                    q.push(make_pair(curr_r, curr_c));
                    visited.insert(make_pair(curr_r, curr_c));
                }
            }
        }
    }
};