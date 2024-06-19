# DSA_progress

Creating this repository to work on the DSA Leetcode problems and track it along the way
total areas to complete
https://neetcode.io/practice

https://github.com/armankhondker/best-leetcode-resources

The goal of this Read me file is to have the Journalling of all the learnings I am gonna make while grinding Leet code and document it so it can easy to revise when ever needed.
This is a 100 days grinding of leetcode.

## Approach for this blind 75

- first watch all the videos of all the problems in that specific pattern
- understand the logical techniques used in problem solving and make a note of them
- visualize the solutions and revise them before jumping into the code
- now once all the problems in that pattern are done, then start solving one by one on my own by checking the logical notes needed

## GOAL - To Complete the Blind 75 List of the coding Questions

# Arrays And Hashing

# Two Pointers

- [ ] **Valid Palindrome**

  - two pointers, check if alpha numeric or not and move the pointers. simple af

- [ ] **3Sum**
  - Sort the input array
  - checking for the first element of the desired output nad for the remaining, use the two sum logic
- [ ] **Container With Most Water**

# Sliding Window

- [ ] **Best Time to Buy and Sell Stock**

- [ ] **Longest Substring without repeating characters**

- [ ] **Longest Repeating character replacement**

- [ ] **Minimum Window Substring**

# Stack

- [ ] **Valid Parenthesis**

# Binary Search

- [ ] **Find Minimum in the rotated binary search**

- [ ] **Search in a rotated Sorted Array**

# Linked List

## Problems from Blind 75

- [x] **Reverse Linked List**

  - two pointers
  - prev and curr
  - change the curr pointing to the prev and increment the pointers till it reaches the end

- [x] **Merge Sorted Lists**

  - create a dummy linked list. compare each value from the each list and the tail points to the least value
  - move to the next item in the list
  - if both lists are not equal, then attach that to the tail of the output list.

- [x] **Reorder List**

  - first find the middle. use **slow and fast pointers** to find the middle
  - reverse the second half of the linked list. create a None as prev and then start reversing
  - now merge the two halfs, using two pointers for two halfs and two temporary variables to store the next values

- [x] **Remove Nth Node from the End of the List**

  - Just create a Dummy node. creating this means, adding 0 to the head of the given list. dummy = Listnode(0, head)
    Use two Pointers, start the left from the dummy node. right one starts with the n nodes from the head given in the question
  - move the pointers until the right points to None
  - then just point the next of the left to the left.next

- [x] **Linked List Cycle**
  - use two pointers, slow and fast technique
