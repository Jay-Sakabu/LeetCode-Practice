#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../../c-utils/colors.h"

/*
    This solution takes advantage of qsort() from the C Standard Library. 
*/

int compare(const void *a, const void *b)
{
    return strcmp((char *)a, (char *)b);
}

int anagram(char *s, char *t)
{
    int result;
    if (strlen(s) != strlen(t))
    {
        return 0; // Not anagrams if lengths differ
    }
    //Create copies of the original strings to not alter the originals
    char *s1_copy = strdup(s);
    char *s2_copy = strdup(t);

    qsort(s1_copy, strlen(s1_copy), sizeof(char), compare);
    qsort(s2_copy, strlen(s2_copy), sizeof(char), compare);
    result = strcmp(s1_copy, s2_copy) == 0;

    free(s1_copy);
    free(s2_copy);
    return result; // Return 1 if anagrams, 0 otherwise
}

void checkAnagram(char *s1, char *s2)
{
    if (anagram(s1, s2))
    {
        printf(KGRN "The strings '%s' and '%s' are anagrams.\n" KRESET, s1, s2);
    }
    else
    {
        printf(KRED "The strings '%s' and '%s' are not anagrams.\n" KRESET, s1, s2);
    }
}

int main()
{
    char s1[] = "metalgear";
    char s2[] = "lategamer";
    char s3[] = "hello";
    checkAnagram(s1, s2);
    checkAnagram(s1, s3);
    checkAnagram("", "jaysakabu");
    checkAnagram("","");
}