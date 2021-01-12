# https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1/?track=md-string&batchId=144
# 5. Check if string is rotated by two places
# Basic Accuracy: 41.08% Submissions: 20801 Points: 1

# Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places.

# Example 1:

# Input:
# a = amazon
# b = azonam
# Output: 1
# Explanation: amazon can be rotated anti
# clockwise by two places, which will make
# it as azonam.

# Your Task:
# The task is to complete the function isRotated() which takes two strings as input parameters and checks if given strings can be formed by rotations. The function returns true if string 1 can be obtained by rotating string 2 by two places, else it returns false.

# Expected Time Complexity: O(N).
# Expected Space Complexity: O(N).
# Challenge: Try doing it in O(1) space complexity.

def isRotated(s, p):
    
    n = len(s)
    if (len(s)==len(p)):
        if (n==1 or n==2) and s==p:
            return True

        x = s+s

        if (p==x[2:n+2]) or (p==x[n-2:n+4]):
            return True

    return False