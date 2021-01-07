# Union of two arrays
# https://practice.geeksforgeeks.org/problems/union-of-two-arrays/0#
# Basic Accuracy: 47.91% Submissions: 40672 Points: 1

# Given two arrays A and B of size N and M respectively. The task is to find union between these two arrays.
# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in union.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consist of three lines. The first line of each test case contains two space separated integers N and M, where N is the size of array A and M is the size of array B. The second line of each test case contains N space separated integers denoting elements of array A. The third line of each test case contains M space separated integers denoting elements of array B.

# Output:
# Correspoding to each test case, print the count of union elements of the two arrays.

# Expected Time Complexity: O(N + M).
# Expected Auxiliary Space: O(N + M).

def Union(A, B, n, m):
    li = []
    
    for i in range(n):
        if A[i] not in li:
            li.append(A[i])
    
    for j in range(m):
        if B[j] not in li:
            li.append(B[j])
    
    return len(li)
    

t = int(input())

for i in range(t):
    size = list(map(int, input().split()))
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    l = Union(A, B, size[0], size[1])
    
    print(l)