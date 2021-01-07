// https://practice.geeksforgeeks.org/problems/palindrome-string0817/1#
// Palindrome String
// School Accuracy: 50.89% Submissions: 10119 Points: 0

// Given a string S, check if it is palindrome or not.

// Example 1:

// Input: S = "abba"
// Output: 1
// Explanation: S is a palindrome

// Example 2:

// Input: S = "abc" 
// Output: 0
// Explanation: S is not a palindrome

 

// Your Task:  
// You don't need to read input or print anything. Complete the function isPlaindrome() which accepts string S and returns a boolean value


// Expected Time Complexity: O(Length of S) 
// Expected Auxiliary Space: O(1) 

// Way 1 using in-built python function:

def isPlaindrome(self, S):
		
		if S==S[::-1]:
		    return 1
		    
		return 0

// Way 2

	int isPlaindrome(string S)
	{
	    int ct = 1;
	    int n = S.size();
	    
	    for (int i=0; i<n/2; i++)
	    {
	        if (S[i]!=S[n-1-i])
	            ct = 0;
	    }
	    
	    if (ct==1)
	    {
	        return 1;
	    }
	    else
	    {
	        return 0;
	    }
	}
