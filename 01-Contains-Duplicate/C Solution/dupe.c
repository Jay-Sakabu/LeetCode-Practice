#include <stdio.h>

/*
 This function uses a nested loop to check for duplicates in an array of integers.
 It returns 1 if duplicates are found, otherwise it returns 0. This is a brute-force approach
*/
int containsDupes(int *nums, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            if (nums[i] == nums[j])
            {
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    int nums[] = {1, 2, 3, 4, 5, 6};     // False
    int nums2[] = {1, 2, 3, 4, 5, 6, 1}; // True
    int nums3[] = {1, 2, 3, 4, 5, 6, 2}; // True

    // Test cases
    // When duplicates occur or not, we want to return true or false.
    // To that end, we can use the ternary operator to print "true" or "false" based on the return value of containsDupes.
    printf("Contains duplicates in nums: %s\n", containsDupes(nums, 6) ? "true" : "false");
    printf("Contains duplicates in nums2: %s\n", containsDupes(nums2, 7) ? "true" : "false");
    printf("Contains duplicates in nums3: %s\n", containsDupes(nums3, 7) ? "true" : "false");

    return 0;
}