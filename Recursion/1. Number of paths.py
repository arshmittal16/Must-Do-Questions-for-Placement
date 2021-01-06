# 1. Number of paths
# https://practice.geeksforgeeks.org/problems/number-of-paths0926/1/?track=md-recursion&batchId=144#
# Basic Accuracy: 65.48% Submissions: 2536 Points: 1

# The problem is to count all the possible paths from top left to bottom right of a MxN matrix with the constraints that from each cell you can either move to right or down.

# Example 1:

# Input:
# M = 3 and N = 3
# Output: 6
# Explanation:
# Let the given input 3*3 matrix is filled 
# as such:
# A B C
# D E F
# G H I
# The possible paths which exists to reach 
# 'I' from 'A' following above conditions 
# are as follows:ABCFI, ABEHI, ADGHI, ADEFI, 
# ADEHI, ABEFI

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function numberOfPaths() which takes the integer M and integer N as input parameters and returns the number of paths..

# Expected Time Complexity: O(m + n - 1))
# Expected Auxiliary Space: O(1)

class Solution:
    def numberOfPaths (self, n, m):
        if n==1 or m==1:
            return 1
        
        return Solution.numberOfPaths(self, n-1, m) + Solution.numberOfPaths(self, n, m-1)
        pass