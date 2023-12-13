"""
Given a nested list of arbitrary depth, write a one-liner to flatten it into a simple list

Example:
l = [1,2,[3,4],[[[5]]], [[6], [[[7]]]]]

flatten(l)
Out[11]: [1, 2, 3, 4, 5, 6, 7]

"""

flatten = lambda l: sum(map(flatten, l), []) if isinstance(l, list) else [l]

# 1. map(flatten, l) applies the flatten function to each item in the list l.
# 2. The sum() function then concatenates these lists together, starting with an empty list [].
# 3. If l is not a list, [l] is returned, wrapping the non-list element in a list.