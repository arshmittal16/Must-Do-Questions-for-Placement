# A Program to check if strings are rotations of each other or not
# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

#     Difficulty Level : Medium
#     Last Updated : 06 Nov, 2020

# Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
# (eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

def areRotations(str1, str2):

    temp = str1 + str1
    if len(str1)!=len(str2):
        return 0

    if temp.count(str2)>0:
        return 1

    return 0
