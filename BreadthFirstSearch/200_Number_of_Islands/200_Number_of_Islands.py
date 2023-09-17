class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        200. Number of Islands
        Solved
        Medium
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
        You may assume all four edges of the grid are all surrounded by water.

        Example 1:
        Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]
        Output: 1
        
        Example 2:
        Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
        Output: 3
        """
        # Use ideas from graphs
        # BFS solution to identify islands (neighbor layers)
    
        # watch this video
        # https://www.google.com/search?q=200.+Number+of+Islands+leetcode+solution+python&rlz=1C1CHBF_enUS894US894&oq=200.+Number+of+Islands+leetcode+solution++python&aqs=chrome..69i57.10689j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_daTyYorGBtyj5NoPleeHkAE25
        
        if not grid:
            return 0
        
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = []
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.pop(0)
                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                for dr, dc in directions:
                    curr_r, curr_c = row + dr, col + dc
                    if curr_r in range(rows) and curr_c in range(cols) and grid[curr_r][curr_c] == '1' and (curr_r,curr_c) not in visited:
                        queue.append((curr_r, curr_c))
                        visited.add((curr_r, curr_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r, c)
                    res += 1
        return res