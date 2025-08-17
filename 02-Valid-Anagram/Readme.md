## Problem Description

[Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

### Examples

**Example 1:**



```
Input:  s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**


```
Input:  s = "rat", t = "car"
Output: false
```

---

### Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

### Follow Up

What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

### Assumptions & Approach


To check if `s` and `t` are anagrams:

1. Check if `s` and `t` have the same length. 
a. If not, they cannot be anagrams. `silent` cannot be an anagram of `listenn`
2. Compare the frequency of each letter in both strings. If all letter counts match, they are anagrams.
a. By sorting the letters in alphabetic order, we can compare the strings
b. `listen` and `silent` arranged alphabetically are both `eilnst`, they are anagrams

### Screenshot of C output
![Vaglrind Verfication](https://drive.google.com/file/d/1LqMipQY-Q9_Jrj_Y0n-TQ_W8t91ubIJZ/view?usp=sharing)