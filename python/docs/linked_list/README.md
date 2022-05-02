# Singly Linked List

A linked list is a data structure that contains nodes that links/points to the next node in the list. A linked list is singly linked if each node in the list has only one reference which points to the Next node in the list.

## Challenge

Creates a LinkedList class that uses a Node class to form a singly linked list. The Node class that has properties for the value stored in the Node, and a pointer to the next Node.

## Approach & Efficiency

With pre-set tests to check for effectiveness in a number of different cases, three methods are built into the LinkedList class:

1. `insert()` to add new nodes with a set value to the list
2. `includes()` to search/query the Nodes on the list for a particular input value
3. `__str__()` to return a string representation of all of the Node values in order along the linked list, ending with a "NULL" value.

Big O Time - The `includes()` and `__str__()` methods have O(n) use of time, as the longer the list the longer the amount of time to search it or produce a string representation of it. The `insert()` method, however, uses O(1) of time because it only ever adds values to the head, so the time resources required will remain constant no matter the input.
Big O Space - I'm actually still unsure if the Big O for Space is the same as for time in this case.
