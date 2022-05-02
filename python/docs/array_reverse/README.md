# Reverse an Array

The challenege is to write a function called `reverseArray` which takes an array as an argument. Without utilizing any of the built-in methods available to your language, it must return an array with elements in reversed order.

## Whiteboard Process

![Whiteboard of Array Reversal](array-reverse.png)

## Approach & Efficiency

Utilized for loops since they can access the elements in an iterative way without needing to use methods. By only looping through a range of half the length of the array, accessing the index element indexes for the first half of the array, and swapping them with the indexes for the second half of the array through negative indexing, the output is the reverse of the input array.
