# 1. Definition:
Greedy algorithms make the best "local" choice at each step, with the hope that these local choices will lead to a globally optimal solution. However, it's worth noting that greedy algorithms do not always yield the best solution for all problems. They are particularly effective when a problem has what's called an "optimal substructure," meaning the problem can be broken down into smaller, simpler subproblems which can be solved independently.

# 2. Optimal Substructure:
"Optimal substructure" is indeed a property that is frequently associated with dynamic programming. In dynamic programming, we break a problem down into smaller subproblems, solve each subproblem, and store its answer. We then combine these subproblem solutions to solve larger problems.

However, the term is also relevant in the context of greedy algorithms. In greedy algorithms, the optimal solution to the problem contains the optimal solutions to the subproblems. The difference is, in greedy algorithms, we don't solve the subproblems independently and combine them. Instead, we make a series of choices, where each choice is the one that seems best at the moment, aiming for an optimal solution to the larger problem.

For example, consider the problem of finding the shortest path from one point to another on a map. An optimal path would have the least distance or time, and this optimal path would consist of segments that are themselves the shortest paths between their end points. In this case, we can say the problem exhibits optimal substructure.

# 3. Choice of Local Optima:
In Gradient Descent, at each step, you update the current point by moving in the direction of the steepest descent (negative of the gradient). This is a form of a greedy choice because you're making a move that minimizes the function value the most at that particular point. You're not looking ahead to see how this choice might affect future steps; you're just making the best local choice.
In the context of greedy algorithms, this kind of local choice is often easier to identify. For instance, in the problem of coin change where you're given denominations 1,5,10,25 and you want to make 33 cents with the least number of coins, your local best choice at each step would be to pick the largest coin denomination that is not greater than the remaining amount you have to make. You keep doing this until you've made the exact amount.

# 4. Iterative vs Recursive Approach: 
Let's consider a simple example problem: the Coin Change problem, where you have unlimited coins of given denominations, and you want to make a change for a given amount using the fewest number of coins. For simplicity, let's say the denominations are [1, 5, 10, 25], and you want to make change for 33 cents.

## Iterative Approach
```
def coin_change_iterative(amount, coins=[1, 5, 10, 25]):
    count = 0
    for coin in reversed(coins):  # Start with the largest coin
        while amount >= coin:
            amount -= coin
            count += 1
    return count

result = coin_change_iterative(33)
print(result)  # Output should be 4 (25 + 5 + 1 + 1 + 1)
```
## Recursive Approach
```
def coin_change_recursive(amount, coins=[1, 5, 10, 25]):
    if amount == 0:
        return 0
    for coin in reversed(coins):
        if amount >= coin:
            return 1 + coin_change_recursive(amount - coin)
    return float('inf')  # This should never be reached for this example

result = coin_change_recursive(33)
print(result)  # Output should be 4 (25 + 5 + 1 + 1 + 1)
```
Both approaches essentially do the same thing but represent different ways of structuring the logic. The iterative approach is usually more efficient because it doesn't have the overhead of recursive function calls.

# Local vs Global Optimum
In a greedy algorithm, at each step, you make a choice that looks the best at that moment, aiming for a local optimum. However, this doesn't always guarantee that you will reach the global optimum (the best possible solution).

### Local Optimum: 
The best solution among all feasible solutions in the immediate neighborhood of a point.

### Global Optimum: 
The best solution among all possible solutions, not just those in a particular neighborhood of a point.

# Greedy Choice Property & Optimal Substructure

**Greedy Choice Property**: A global optimum can be arrived at by selecting a local optimum.

**Optimal Substructure**: An optimal solution to the problem contains optimal solutions to sub-problems.

1. Can you think of a situation where making a locally optimal choice will not lead to a globally optimal solution?
2. Do you know what types of problems are usually good candidates for greedy algorithms?
<a/>

1. Yes, you're correct about the Coin Change problem. If the coin denominations are not carefully chosen, a greedy algorithm that always picks the largest denomination will not necessarily find the minimum number of coins needed for change. For instance, if the denominations are [1, 3, 4] and you need to make 6, the greedy algorithm would choose 4, then 1, then 1, for a total of 3 coins. However, the optimal solution would be two coins: 3 and 3. Dynamic Programming would indeed find this optimal solution.
2. Your intuition is spot-on. Problems that are good candidates for greedy algorithms often have an "easy-to-identify" local optimum and can be solved iteratively or recursively while maintaining the optimality condition.

