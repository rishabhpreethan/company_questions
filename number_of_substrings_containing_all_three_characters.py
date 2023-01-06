#MEDIUM
# 1358

'''     https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/     '''
'''     https://youtu.be/VNL2VhDxj7U        '''

# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.


# Example 1:
# Input: s = "abcabc"
# Output: 10
# ---------------------------------------------------
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

# Example 2:
# Input: s = "aaacb"
# Output: 3
# ----------------------------------------------------
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

# Example 3:
# Input: s = "abc"
# Output: 1


def numberOfSubstrings(s):
    count=0
    a=-1
    b=-1
    c=-1
    for i,x in enumerate(s):
        if x=='a':
            a=i
        elif x=='b':
            b=i
        elif x=='c':
            c=i
        if i>1:
            count+=min([a,b,c])+1
    return count

print(numberOfSubstrings("abcabc"))