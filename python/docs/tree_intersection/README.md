# Tree Intersection

Write a function called tree_intersection that takes two binary trees as parameters.
Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard

![challenge](whiteBoard.png)

## Approach and Efficiency

Use a pre-order traversal to iterate through both trees
convert returned list to a set
call intersection on both sets
return the intersections

Big O:
Time: O(n)
Space: O(n)