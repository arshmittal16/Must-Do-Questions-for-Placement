# 4. Equilibrium Point
# https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1/?track=md-arrays&batchId=144#
# Easy Accuracy: 49.32% Submissions: 41815 Points: 2

# Given an array A of N positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Example 1:

# Input:
# N = 1
# A[] = {1}
# Output: 1
# Explanation: Since its the only 
# element hence its the only equilibrium 
# point. 

# Your Task:
# The task is to complete the function equilibriumPoint() which takes the array and N as input parameters and returns the point of equilibrium. Return -1 if no such point exists.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

def equilibriumPoint(A, N):

    lsum = 0
    rsum = sum(A)
    
    for i in range(N):
        rsum -= A[i]
        
        if lsum==rsum:
            return i+1
        else:
            lsum += A[i]
    
    return -1