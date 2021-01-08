# https://practice.geeksforgeeks.org/problems/remove-duplicates3034/1/?track=md-string&batchId=144#
# 3. Remove Duplicates

# Easy Accuracy: 57.93% Submissions: 4445 Points: 2

# Given a string without spaces, the task is to remove duplicates from it.

# Note: The original order of characters must be kept the same. 

# Example 1:

# Input: S = "geeksforGeeks"
# Output: geksfor
# Explanation: Only keep the first
# occurrence

# Example 2:

# Input: S = "gfg"
# Output: gf
# Explanation: Only keep the first
# occurrence

# Your task:
# Your task is to complete the function removeDups() which takes a single string as input and returns the string. You need not take any input or print anything.

def removeDups(self, S):
		narr = []
		
		for i in range(len(S)):
		    if S[i] not in narr:
		        narr.append(S[i])
	    
	    narr = str("".join(narr))
		
		return narr