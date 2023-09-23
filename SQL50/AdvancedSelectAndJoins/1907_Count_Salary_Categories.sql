'
    1907. Count Salary Categories
    Solved
    Medium
    Topics
    Companies
    SQL Schema
    Pandas Schema
    Table: Accounts

    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | account_id  | int  |
    | income      | int  |
    +-------------+------+
    account_id is the primary key (column with unique values) for this table.
    Each row contains information about the monthly income for one bank account.
    

    Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

    "Low Salary": All the salaries strictly less than $20000.
    "Average Salary": All the salaries in the inclusive range [$20000, $50000].
    "High Salary": All the salaries strictly greater than $50000.
    The result table must contain all three categories. If there are no accounts in a category, return 0.

    Return the result table in any order.

    The result format is in the following example.

    

    Example 1:

    Input: 
    Accounts table:
    +------------+--------+
    | account_id | income |
    +------------+--------+
    | 3          | 108939 |
    | 2          | 12747  |
    | 8          | 87709  |
    | 6          | 91796  |
    +------------+--------+
    Output: 
    +----------------+----------------+
    | category       | accounts_count |
    +----------------+----------------+
    | Low Salary     | 1              |
    | Average Salary | 0              |
    | High Salary    | 3              |
    +----------------+----------------+
    Explanation: 
    Low Salary: Account 2.
    Average Salary: No accounts.
    High Salary: Accounts 3, 6, and 8.
'
# Write your MySQL query statement below
with SalaryCategories as (
    select case when income < 20000 then 'Low Salary' when income between 20000 and 50000 then 'Average Salary' else 'High Salary' end as category
    from Accounts
)

select 'Low Salary' as category, coalesce(sum(case when category = 'Low Salary' then 1 else 0 end), 0) as accounts_count
from SalaryCategories
union
select 'Average Salary', coalesce(sum(case when category = 'Average Salary' then 1 else 0 end), 0)
from SalaryCategories
union
select 'High Salary', coalesce(sum(case when category = 'High Salary' then 1 else 0 end), 0)
FROM SalaryCategories
