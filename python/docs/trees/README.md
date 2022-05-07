# Trees

## Challenge

Creates a Node class, Binary Tree class, and a Binary Search Tree (BST) subclass of Binary Tree class.

The Node class has properties of:

1. value stored in the node
2. the left child node
3. the right child node

The Binary Tree class has defined methods for depth first traversals of type:

1. pre-order
2. in-order
3. post-order

- these methods return a list of the values, ordered accordingly to the respective traversal type

The BST subclass has two additional methods unique to it:

1. add: takes an input value and adds a new node containing that input value in the appropriate location for a binary search tree
2. contains: takes an input value and return a boolean indicating whether the input value is contained in the tree at least once

## Approach & Efficiency

The Node class is given a dunder init method to give it the properties of value, left, and right.

The Binary Tree class is given three methods which follow the same pattern, changing only the order of whether to traverse root >>> left >>> right (for pre-order), left >>> root >>> right (for in-order), or left >>> right >>> root. The methods each respectively traverse in their designated order, and record the values of each node by appending them into a list, which is then returned as the final line of action of the method (unless it is an empty tree).

The Binary Search Tree subclass is given an add method and a contains method.

- The add method assigns an `input_node` to be of class Node containing the input value as its value. If being added to an empty tree, it is added as the root Node. Otherwise, a `traverse()` method is called with a base case that either (1) returns if there is no root node, (2) if the root node's value is greater than the input_node then it either assigns the input_node as the left child if there isn't one already or recursively calls the traverse() method on the existing left child, (3) otherwise does the same for the right child.
- The contains method takes in the tree and a search value. If there is no root node for the tree, it just returns False because it's an empty tree. Otherwise, a `traverse()` method is returned that either (1) returns True if the value of the root node is equal to the input search value, (2) if the root node value is greater than search value and there is a left child of the root node then the traverse() method is called with the left child as input and its output is returned, (3) if the root node value is less than the search value then the same is done for the right child, (4) otherwise the traverse method returns False because the entire height of the tree has been traversed and the search value was not found contained by any of the Nodes.

### Big O

Big O time complexity for each of the three Binary Tree depth first traversal methods is O(n) where n is the number of nodes, because the entire tree will need to be traversed for the list of each Node's values to be produced and returned. Big O space complexity for each method will be O(w) where w is the largest width of the tree.

Big O time complexity for both the add and contains methods is O(h) where h is equal to the height of the tree. If the tree is "perfectly" balanced such that each non-leaf node has two children, then the height of the tree is log(n) where n is the number of nodes. Otherwise, the worst case scenario of the tree's height is n (i.e. O(height) = O(n)). Without knowing the balance of the tree, then we accept worst case scenario, so **time complexity is O(n)**. Big O space complexity is O(1) because there is always just one single clear path down down the tree with no additional space needed.
