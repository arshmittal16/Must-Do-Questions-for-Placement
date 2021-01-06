# 11. Kth smallest element
# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1#
# Medium Accuracy: 46.66% Submissions: 15928 Points: 4

# Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Expected Time Complexity: O(n)

# Input:
# The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case consists of three lines. First line of each testcase contains an integer N denoting size of the array. Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.

# Output:
# For each testcase, in a newline, print the kth smallest element.

# Yout Task:
# Complete kthSmallest and return the kth smallest element. 

# There are 2 ways to do this:

# Way 1:

def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    arr.sort()
    
    return arr[k-1]

## Way 2:

def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    minm = min(arr)
    
    for i in range(k-1):
        arr.remove(minm)
        minm = min(arr)
        
    return minm
    