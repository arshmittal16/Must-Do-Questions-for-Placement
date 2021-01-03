# 1. Missing number in array: 
# https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1/?track=md-arrays&batchId=144
# Easy Accuracy: 42.51% Submissions: 19362 Points: 2

# Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N.
# Find the missing element.

# Example 1:

# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4

# Your Task :
# Complete the function MissingNumber() that takes array and N as input and returns the value of the missing number.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).


def MissingNumber(array,n):
    
    array.sort()
    
    if n == 2:
        if array[0]!=1:
            return 1
        else:
            return 2
            
    for i in range(0,n-1):
        if (i+1)!=array[i]:
            return (i+1)
        else:
            continue
        
    if array[n-2] == n-1:
        return n
