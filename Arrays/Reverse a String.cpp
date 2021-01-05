// Reverse a String
// https://practice.geeksforgeeks.org/problems/reverse-a-string/1#
// Basic Accuracy: 60.35% Submissions: 9674 Points: 1

// You are given a string s. You need to reverse the string.

// Example 1:

// Input:
// s = Geeks
// Output: skeeG

// Your Task:

// You only need to complete the function reverseWord() that takes s as parameter and returns the reversed string.

// Expected Time Complexity: O(|S|).
// Expected Auxiliary Space: O(1).

string reverseWord(string str){
    
    int x = str.size();
    
    for (int i=0; i < x/2 ; i++)
    {
        swap(str[i], str[x-i-1]);
    }
    
    return str;
}