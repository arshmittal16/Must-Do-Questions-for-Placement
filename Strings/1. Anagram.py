# 1. Anagram
# https://practice.geeksforgeeks.org/problems/anagram-1587115620/1/?track=md-string&batchId=144#
# Easy Accuracy: 50.99% Submissions: 15335 Points: 2

# Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “act” and “tac” are an anagram of each other.

# Example 1:

# Input:
# a = geeksforgeeks, b = forgeeksgeeks
# Output: YES
# Explanation: Both the string have same
# characters with same frequency. So, 
# both are anagrams.

# Your Task:
# You don't need to read input or print anything.Your task is to complete the function isAnagram() which takes the string a and string b as input parameter and check if the two strings are an anagram of each other. The function returns true if the strings are anagram else it returns false.

# Expected Time Complexity: O(|a|+|b|).
# Expected Auxiliary Space: O(Number of distinct characters).

def isAnagram(a,b):
    
    if len(b) == len(a):
        for i in range(len(a)):
            if a[i] in b:
                continue
            else:
                return False
    else:
        return False

    return True