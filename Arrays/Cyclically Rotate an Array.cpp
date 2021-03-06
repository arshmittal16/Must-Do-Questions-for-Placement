// Cyclically rotate an array by one
// https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0#
// Basic Accuracy: 49.41% Submissions: 35740 Points: 1

// Given an array, cyclically rotate an array by one.

// Input:
// The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. Then following line contains 'n' integers forming the array. 

// Output:
// Output the cyclically rotated array by one.

// Constraints:
// 1<=T<=1000
// 1<=N<=1000
// 0<=a[i]<=1000

// Example:
// Input:
// 2
// 5
// 1 2 3 4 5
// 8
// 9 8 7 6 4 2 1 3

// Output:
// 5 1 2 3 4
// 3 9 8 7 6 4 2 1

#include <iostream>
using namespace std;

void rotate(int arr[], int n)
{
    int temp = arr[n-1];
    
    for (int i = n-1; i>0; i--)
    {
        arr[i] = arr[i-1];
    }
    
    arr[0] = temp;
    
    for (int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }
}

int main() {
	int t;
	cin>>t;
	
	for (int i=0;i<t;i++)
	{
	    int n;
	    cin>>n;
	    int arr[n];
	    
	    for (int j=0; j<n; j++)
	    {
	        cin>>arr[j];
	    }
	    
	    rotate(arr, n);
	    
	    cout<<endl;
	    
	}
	return 0;
}