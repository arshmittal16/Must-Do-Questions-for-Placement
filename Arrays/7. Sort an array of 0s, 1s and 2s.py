# 7. Sort an array of 0s, 1s and 2s
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1/?track=md-arrays&batchId=144#
# Easy Accuracy: 51.36% Submissions: 32788 Points: 2

# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output: 0 0 1 2 2
# Explanation: 0s 1s and 2s are segregated 
# into ascending order.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function sort012() that takes array and n as input parameters and sorts the array in-place. 

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

def sort012(arr,n):
    arr.sort()

## Without using any inbuilt function

def sort012(arr,n):
    c0, c1, c2 = 0, 0, 0
    
    for i in range(n):
        if arr[i] == 0:
            c0 += 1
        elif arr[i] == 1:
            c1 += 1
        else:
            c2 += 1
        
    for i in range(c0):
        arr[i] = 0
    
    for i in range(c1):
        arr[c0 + i] = 1
    
    for i in range(c2):
        arr [c0 + c1 + i] = 2
        
    return arr