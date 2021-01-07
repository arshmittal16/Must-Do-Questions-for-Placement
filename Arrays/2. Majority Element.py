# 2. Majority Element
# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1/?track=md-arrays&amp;batchId=144#
# Basic Accuracy: 48.6% Submissions: 24771 Points: 1

# Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

# Example 1:

# Input:
# N = 3 
# A[] = {1,2,3} 
# Output: -1

# Explanation: Since, each element in 
# {1,2,3} appears only once so there 
# is no majority element.

# Your Task:
# The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).

## Way 1

def majorityElement(arr,n):
    
    arr.sort()

    if n==1:
        return arr[0]
        
    count = 1
    maxe = -1
    temp= arr[0]

    for i in range(1, n):
        
        if(temp == arr[i]):
            count += 1
        else :
            count = 1
            temp = arr[i]
            
        if(maxe < count) :
            maxe = count
            element = arr[i]
            
            if(maxe > (n//2)) :
                return element
    return -1
            
## Way 2

def majorityElement(arr,n):
    arr.sort()

    for i in range(n):
        if (arr.count(arr[i])>n/2):
            return arr[i]

    return -1
    