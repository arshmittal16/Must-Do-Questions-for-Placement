# 5. Largest subarray of 0's and 1's
# https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1/?track=md-arrays&batchId=144
# Easy Accuracy: 38.92% Submissions: 49169 Points: 2

# Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.

# Example 1:

# Input:
# N = 4
# A[] = {0,1,0,1}
# Output: 4
# Explanation: The array from index [0...3]
# contains equal number of 0's and 1's.
# Thus maximum length of subarray having
# equal number of 0's and 1's is 4.

def maxLen(arr, N):
    
    for i in range(N):
        if arr[i]==0: arr[i] = -1  
    
    sum = 0
    maxe = 0
    
    dic = {}
    
    for i in range(N):
        sum += arr[i]
        
        if sum == 0:
            maxe = i+1
        if sum in dic:
            maxe = max(i-dic[sum], maxe)
        else:
            dic[sum] = i
    
    return maxe 