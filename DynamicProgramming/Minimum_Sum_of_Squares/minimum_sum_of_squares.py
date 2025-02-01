# Recursive implementation (slower)
def minSquares_recursive(n):
    """
        𝗣𝗿𝗼𝗯𝗹𝗲𝗺
        Find the minimum number of perfect squares that sum up to a number 𝙣.

        𝗖𝗼𝗺𝗽𝗮𝗿𝗶𝘀𝗼𝗻
        Recursion: ~25 seconds for 𝙣 = 50
        Dynamic programming: 0.00015 seconds for 𝙣 = 50

        𝗞𝗲𝘆 𝗧𝗮𝗸𝗲𝗮𝘄𝗮𝘆
        Dynamic programming avoids redundant calculations, saves time, and simplifies problem-solving. Start small (e.g., Fibonacci) and progress to more advanced problems like Knapsack or LCS.

        𝗧𝗿𝗮𝗱𝗲𝗼𝗳𝗳
        - Dynamic programming requires higher memory usage and complexity when designing efficient state transitions.
        - Recursion uses more memory and is inefficient for large inputs. In Python, the default recursion depth limit is 1000, and exceeding it raises a RecursionError.  
    """
    if n == 0:
        return 0
    return min(1 + minSquares_recursive(n-k*k) for k in range(1, int(n**0.5) + 1))

# Dynamic Programming implementation bottom-up (faster)
def minSquares_dp(n):
    dp = [0] + [float('inf')] * n
    for i in range(1, n + 1):
        dp[i] = min(1 + dp[i - k * k] for k in range(1, int(i**0.5) + 1))
    return dp[n]


# Dynamic Programming implementation top-down (faster)
# This approach will be much faster than the pure recursive solution 
# while being more intuitive than the bottom-up DP approach for many developers. 
# However, it will still be slightly slower than the bottom-up version due to the overhead of recursive calls.
def minSquares_memoization(n: int, memo: dict = None) -> int:
    # Initialize memo dictionary on first call
    if memo is None:
        memo = {}
    
    # Base cases
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    
    # Calculate minimum squares needed
    min_squares = float('inf')
    for k in range(1, int(n**0.5) + 1):
        min_squares = min(min_squares, 1 + minSquares_memoization(n - k*k, memo))
    
    # Store result in memo before returning
    memo[n] = min_squares
    return min_squares