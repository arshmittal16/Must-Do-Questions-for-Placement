# Reverse words in a given string
# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1/?track=md-string&batchId=144#
# Easy Accuracy: 50.0% Submissions: 26286 Points: 2

# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Example 1:

# Input:


# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i

# Your Task:
# You dont need to read input or print anything. Complete the function reverseWords() which takes string S as input parameter and returns a string containing the words in reversed order. Each word in the returning string should also be separated by '.' 

# Expected Time Complexity: O(|S|)
# Expected Auxiliary Space: O(|S|)

def reverseWords(S):
    li = (S.split('.'))
    lis = []
    y = len(li)

    for i in range(y):
        lis.append(li[y-i-1])
    
    st = str(".".join(lis))
    
    return st