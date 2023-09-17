class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        
        int n = isConnected.size();
        set<int> visited;
        int res = 0;
        for(int i=0; i<n; i++) {
            auto pos = visited.find(i);
            if(pos == visited.end()) {
                bfs(i, visited, isConnected, n);
                res++;
            }
        }
        return res;       
    }
private: 
    void bfs(int i, set<int>& visited, vector<vector<int>>& isConnected, int n) {
        queue<int> q;
        q.push(i);
        while(!q.empty()) {    
            int curr = q.front();
            q.pop();
            visited.insert(curr);
            for(int j=0; j<n; j++) {
                auto pos = visited.find(j);
                if(isConnected[curr][j] == 1 && pos == visited.end()) {
                    q.push(j);
                    visited.insert(j);
                }
            }
        }
    }
};