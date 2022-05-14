# Stacks Queue Animal Shelter

Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.

## Challenge

Implements the following methods:

- enqueue
  - Arguments: animal
    - animal can be either a dog or a cat object.
- dequeue
  - Arguments: pref
    - pref can be either "dog" or "cat"
  - Return: either a dog or a cat, based on preference.
    - If pref is not "dog" or "cat" then return null.

## Whiteboard Process

![Stack Queue Animal Shelter Whiteboard](./stack_queue_animal_shelter_WB.png)

## Approach & Efficiency

### Approach

#### Enqueue method

- function takes in object
- checks if type is Dog or Cat
- add object to respective queue
- if other type, adds nothing

#### Dequeue method

- function takes in string
- checks if pref string is 'dog' or 'cat'
- returns first object in respective queue
- if other pref specified, returns nothing

### Efficiency

- Time: O(1); efficiency will not vary, no matter how many elements are in the queue
- Space: O(1): efficiency will not vary, no matter how many elements are in the queue
