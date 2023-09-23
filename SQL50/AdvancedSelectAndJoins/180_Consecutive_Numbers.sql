'
    180. Consecutive Numbers
    Solved
    Medium
    Topics
    Companies
    SQL Schema
    Pandas Schema
    Table: Logs

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | num         | varchar |
    +-------------+---------+
    In SQL, id is the primary key for this table.
    id is an autoincrement column.
    

    Find all numbers that appear at least three times consecutively.

    Return the result table in any order.

    The result format is in the following example.

    

    Example 1:

    Input: 
    Logs table:
    +----+-----+
    | id | num |
    +----+-----+
    | 1  | 1   |
    | 2  | 1   |
    | 3  | 1   |
    | 4  | 2   |
    | 5  | 1   |
    | 6  | 2   |
    | 7  | 2   |
    +----+-----+
    Output: 
    +-----------------+
    | ConsecutiveNums |
    +-----------------+
    | 1               |
    +-----------------+
    Explanation: 1 is the only number that appears consecutively for at least three times.
'
# Write your MySQL query statement below
select distinct a.num as ConsecutiveNums
from Logs a, Logs b, Logs c
where a.id = b.id - 1
and a.id = c.id - 2
and a.num = b.num 
and a.num = c.num
