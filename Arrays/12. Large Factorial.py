# https://practice.geeksforgeeks.org/problems/large-factorial4721/1/?track=md-arrays&batchId=144#
# 12. Large Factorial
# Medium Accuracy: 57.18% Submissions: 158 Points: 4

# You are given an array A of integers of length N. You need to calculate factorial of each number. The answer can be very large, so print it modulo 109 + 7.
 

# Example 1:

# Input:
# N = 5
# A[] = {0, 1, 2, 3, 4}
# Output:
# 1 1 2 6 24
# Explanation:
# Factorial of 0 is 1, 
# factorial of 1 is 1, factorial of 2 is 2, 
# factorial of 3 is 6 and so on.

# Example 2:

# Input:
# N = 3
# A[] = {5, 6, 3}
# Output:
# 120 720 6
# Explanation:
# Factorial of 5 is 120, 
# factorial of 6 is 720, 
# factorial of 3 is 6.


# Your Task:
# Complete the function factorial() which takes list a and single integer n, as input parameters and returns a list of factorials of the numbers in the list a.


# Expected Time Complexity: O(max(A) + N)
# Expected Auxiliary Space: O(max(A))

def factorial(self,a, n):
    	
    	mod = 1000000007
    	size = 1000000
    	fact = [1]*size
    	
    	for i in range(1, size):
    	    fact[i] = (fact[i-1]*i)%mod
    	
    	for i in range(n):
    	    
    	    x = a[i]
    	    y = fact[x]
    	    
    	    a[i] = y
    	    
    	return a
