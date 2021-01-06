# Middle of Three
# https://practice.geeksforgeeks.org/problems/middle-of-three2926/1#
# Basic Accuracy: 50.22% Submissions: 13362 Points: 1

# Given three distinct numbers A, B and C. Find the number with value in middle (Try to do it with minimum comparisons).


# Example 1:

# Input:
# A = 978, B = 518, C = 300
# Output:
# 518
# Explanation:
# Since 518>300 and 518<978, so 
# 518 is the middle element.

# Your Task:
# You don't need to read input or print anything.Your task is to complete the function middle() which takes three integers A,B and C as input parameters and returns the number which has middle value.

# Expected Time Complexity:O(1)
# Expected Auxillary Space:O(1)

# Since we have to do this in minimum number of comparsons and Space and Time Complexity should be kept O(1)

def middle(self,A,B,C):
        
        x = A-B
        y = B-C
        z = C-A
        
        if x*y > 0:
            return B
        elif y*z > 0:
            return C
        else: 
            return A