
# 0125 - Valid Palindrome

- **Platform:** LeetCode
- **Problem:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **Topic:** Strings, Two Pointers
- **Language:** Python

## Problem Description

Given a string `s`, determine whether it is a palindrome after considering only alphanumeric characters and ignoring differences between uppercase and lowercase letters.

Return `True` if it is a palindrome; otherwise, return `False`.

## Examples

**Example 1**

Input:
```python
s = "A man, a plan, a canal: Panama"
```

Output:
```python
True
```

Explanation:

After removing spaces and punctuation and converting to lowercase:

`amanaplanacanalpanama`

It reads the same forward and backward.

**Example 2**

Input:
```python
s = "race a car"
```

Output:
```python
False
```

Explanation:

After cleaning:

`raceacar`

It does not read the same forward and backward.

**Example 3**

Input:
```python
s = " "
```

Output:
```python
True
```

Explanation:

There are no alphanumeric characters to compare, so it is considered a palindrome.

## Approach: Two Pointers

We use two pointers to compare characters from opposite ends of the string.

1. Initialise `left` to `0` and `right` to `len(s) - 1`.
2. Continue while `left < right`.
3. If the left character is not alphanumeric, move `left` one position forward.
4. If the right character is not alphanumeric, move `right` one position backward.
5. Convert both characters to lowercase and compare them.
6. If they are different, return `False`.
7. If they match, move both pointers towards the centre.
8. If all valid characters match, return `True`.

## Python Concepts Used

### 1. Two Pointers

Two pointers allow us to process a string from both ends without creating another string.

### 2. isalnum()

`isalnum()` checks whether a character is a letter or a number.

```python
"A".isalnum()  # True
"5".isalnum()  # True
",".isalnum()  # False
" ".isalnum()  # False
```

### 3. lower()

`lower()` converts uppercase characters into lowercase.

```python
"N".lower()  # "n"
```

This allows case-insensitive comparisons.

### 4. continue

`continue` skips the remaining statements in the current loop iteration and starts the next iteration.

## Complexity Analysis

Let `n` be the length of the input string.

- **Time Complexity: O(n)**

  Each pointer moves towards the centre, so each character is examined at most once.

- **Space Complexity: O(1)**

  We use only two pointers and a constant amount of additional memory.

## Edge Cases Tested

- Empty or whitespace-only string
- String containing punctuation and spaces
- Uppercase and lowercase characters
- Single-character string
- String containing numbers
- String that is not a palindrome

## Key Takeaway

The Two Pointers technique is an efficient way to solve palindrome problems because it allows us to compare characters from both ends without creating an additional cleaned string.
