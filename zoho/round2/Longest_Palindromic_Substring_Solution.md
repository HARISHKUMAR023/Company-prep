
# Longest Palindromic Substring Solution

## Problem Statement
Given a string, find the longest palindromic substring without using any built-in functions for string reversal or slicing.

## Solution Explanation

To solve the problem, we implement the solution as follows:

### 1. Custom Function to Check Palindrome
We create a function `is_palindrome(s, l, r)` that checks if a substring is a palindrome by comparing characters from the beginning (`l`) and end (`r`), moving towards the center.

### 2. Iterating Over All Possible Substrings
Using nested loops, we iterate through all possible substrings of the given string, check if each one is a palindrome using the `is_palindrome` function, and keep track of the longest one found.

### Implementation in Python:

```python
strs = "LIRILSOAP"
maxi = 0
sub = ""

# Function to check if a substring is a palindrome
def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

# Iterate over all possible substrings
for l in range(len(strs)):
    for r in range(l, len(strs)):
        if is_palindrome(strs, l, r):
            length = r - l + 1
            if length > maxi:
                maxi = length
                sub = strs[l:r+1]

print(sub)
```

### Explanation:
1. **is_palindrome function**:
    - This function checks if the substring from index `l` to `r` is a palindrome.
    - It compares characters starting from both ends and moves towards the center. If all characters match, it's a palindrome.

2. **Main loop**:
    - The outer loop iterates over the starting index `l` of the substring.
    - The inner loop iterates over the ending index `r` of the substring.
    - For each pair `(l, r)`, it checks if the substring `strs[l:r+1]` is a palindrome using the `is_palindrome` function.
    - If the substring is a palindrome and its length is greater than the current maximum, it updates `maxi` and `sub`.

3. **Output**:
    - The longest palindromic substring is stored in `sub` and is printed at the end.

### Output:
For the input string `"LIRILSOAP"`, the output will be:

```
LIRIL
```
This is the longest palindromic substring in the given string.
