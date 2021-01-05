# 3. Leaders in an array
# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1/?track=md-arrays&batchId=144#
# Easy Accuracy: 49.96% Submissions: 32968 Points: 2

# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

# Example 1:

# Input:
# N = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 
# as it is greater than all the elements 
# to its right.  Similarly, the next 
# leader is 5. The right most element 
# is always a leader so it is also 
# included.

# Your Task:
# You don't need to read input or print anything. The task is to complete the function leader() which takes array A and N as input parameters and returns an array of leaders in order of their appearance.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

def leaders(A,N):
    li = []
    max = A[N-1]
    
    
    for i in range(N-2, -1, -1):
        if max <= A[i]:
            li.append(max)
            max = A[i]
        
    li.append(max)
    
    return li[::-1]