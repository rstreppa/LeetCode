class Solution(object):
    from collections import deque
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        397. Integer Replacement
        Medium
        Given a positive integer n, you can apply one of the following operations:

        If n is even, replace n with n / 2.
        If n is odd, replace n with either n + 1 or n - 1.
        Return the minimum number of operations needed for n to become 1.

        Example 1:
        Input: n = 8
        Output: 3
        Explanation: 8 -> 4 -> 2 -> 1

        Example 2:
        Input: n = 7
        Output: 4
        Explanation: 7 -> 8 -> 4 -> 2 -> 1
        or 7 -> 6 -> 3 -> 2 -> 1

        Example 3:
        Input: n = 4
        Output: 2
        """
        queue = deque([(n, 0)])  # Initialize the queue with the tuple (n, steps)
        visited = set([n])       # To keep track of visited nodes
        
        while queue:
            cur, steps = queue.popleft()
            
            if cur == 1:
                return steps
            
            if cur % 2 == 0:
                next_val = cur // 2
                if next_val not in visited:
                    queue.append((next_val, steps + 1))
                    visited.add(next_val)
                    
            else:
                for next_val in [cur + 1, cur - 1]:
                    if next_val not in visited:
                        queue.append((next_val, steps + 1))
                        visited.add(next_val)
