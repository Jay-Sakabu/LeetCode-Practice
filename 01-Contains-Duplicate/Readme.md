## Problem Description

[Contains Duplicates](https://leetcode.com/problems/contains-duplicate/description/): Given an integer array `nums`, return `true` if any value appears at least twice in the array. Return `false` if every element is distinct.

## Examples

**Example 1**

- **Input:** `nums = [1,2,3,1]`
- **Output:** `true`
- **Explanation:** The element `1` appears at indices 0 and 3.

**Example 2**

- **Input:** `nums = [1,2,3,4]`
- **Output:** `false`
- **Explanation:** All elements are unique.

**Example 3**

- **Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`
- **Output:** `true`

## Assumptions

These solutions focus solely on whether duplicates exist in the array, regardless of which values are repeated. That is, we do not keep track of _which_ values are duplicates.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`