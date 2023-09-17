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

        # Number of cities
        n = len(isConnected)
        
        # To keep track of visited cities
        visited = set()
        
        # Initialize the result to zero
        res = 0
        
        # Function to perform DFS from a given city i
        def dfs(i):
            # Mark the city as visited
            visited.add(i)
            
            # Go through all other cities
            for j in range(n):
                # If city j is connected to i and j has not been visited yet
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
        
        # Go through all cities
        for i in range(n):
            # If the city has not been visited yet, it means it's a new province
            if i not in visited:
                dfs(i)
                res += 1
                
        
        return res