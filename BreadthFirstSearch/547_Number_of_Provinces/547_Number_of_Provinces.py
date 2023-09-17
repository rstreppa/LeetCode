from collections import deque

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int

        547. Number of Provinces
        Solved
        Medium
        There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
        and city b is connected directly with city c, then city a is connected indirectly with city c.
        A province is a group of directly or indirectly connected cities and no other cities outside of the group.
        You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
        and isConnected[i][j] = 0 otherwise.

        Return the total number of provinces.

        Example 1:
        Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        Output: 2

        Example 2:
        Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        Output: 3
        """

        # Use ideas from graphs
        # BFS solution to identify islands (neighbor layers)
        # Study the solution of 200. Number of Islands, solution kind of similar
        # The problem seems to be that you're approaching the problem as a 2D grid when in fact, 
        # it's just a representation of a graph.         
        # The isConnected[i][j] value tells you whether city i is connected to city j. Since it's a graph, 
        # you don't need to consider "up", "down", "left", or "right" neighbors, as you would do in a 2D grid problem.

        # This code uses BFS to explore each province. It starts the BFS from each unvisited city, 
        # marking all cities in the same province as visited. Each time we start a new BFS, we increase the province count by 1.

        # Number of cities
        n = len(isConnected)
        
        # To keep track of visited cities
        visited = set()
        
        # Initialize the result to zero
        res = 0
        
        # Function to perform BFS from a given city i
        def bfs(i):
            # Create a queue and enqueue the starting city
            queue = deque([i])
            
            while queue:
                # Dequeue a city from the front of the queue
                curr = queue.popleft()
                
                # Mark the city as visited
                visited.add(curr)
                
                # Enqueue all connected, not-yet-visited cities
                for j in range(n):
                    if isConnected[curr][j] == 1 and j not in visited:
                        queue.append(j)
                        visited.add(j)  # Mark the city as visited as soon as it's enqueued
        
        # Go through all cities
        for i in range(n):
            # If the city has not been visited yet, it means it's a new province
            if i not in visited:
                bfs(i)
                res += 1
                
        
        return res