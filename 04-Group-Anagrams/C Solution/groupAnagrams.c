#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../c-utils/colors.h"

#define HASH_SIZE 50000
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
typedef struct Entry
{
    char *key;
    char **values;
    int valuesSize;
    struct Entry *next;
} Entry;

Entry *createEntry(char *key)
{
    Entry *entry = (Entry *)malloc(sizeof(Entry));
    entry->values = (char **)malloc(10000 * sizeof(char *));
    entry->key = key;
    entry->valuesSize = 0;
    entry->next = NULL;
    return entry;
}

int hash(char *string)
{
    int hash = 0;
    while (*string)
    {
        hash = (hash * 31 + (*string++)) % HASH_SIZE;
    }
    return hash;
}
// Pretty standard comparison function for qsort
int compare(const void *a, const void *b)
{
    return (*(char *)a - *(char *)b);
}

char ***groupAnagrams(char **strs, int strsSize, int *returnSize, int **returnColumnSizes)
{
    Entry **hashTable = (Entry **)calloc(HASH_SIZE, sizeof(Entry *));
    char ***result = (char ***)malloc((size_t)strsSize * sizeof(char **)); //Explicit cast to size_t to avoid warning
    *returnColumnSizes = (int *)malloc((size_t)strsSize * sizeof(int));
    *returnSize = 0;

    for (int i = 0; i < strsSize; i++)
    {
        char *sortedStr = strdup(strs[i]);
        qsort(sortedStr, strlen(sortedStr), sizeof(char), compare);
        int index = hash(sortedStr);

        Entry *entry = hashTable[index];
        while (entry)
        {
            if (strcmp(entry->key, sortedStr) == 0)
            {
                entry->values[entry->valuesSize++] = strs[i];
                break;
            }
            entry = entry->next;
        }

        if (!entry)
        {
            Entry *newEntry = createEntry(sortedStr);
            newEntry->values[newEntry->valuesSize++] = strs[i];
            newEntry->next = hashTable[index];
            hashTable[index] = newEntry;
        }
        else
        {
            free(sortedStr);
        }
    }

    for (int i = 0; i < HASH_SIZE; i++)
    {
        Entry *entry = hashTable[i];
        while (entry)
        {
            result[*returnSize] = entry->values;
            (*returnColumnSizes)[*returnSize] = entry->valuesSize;
            (*returnSize)++;
            Entry *temp = entry;
            entry = entry->next;
            free(temp->key);
            free(temp->values); // Free the values array
            free(temp);
        }
    }

    free(hashTable);
    return result;
}

int main(void)
{
    char *strs[] = {"eat", "tea", "tan", "ate", "nat", "bat"};
    int strsSize = sizeof(strs) / sizeof(strs[0]);
    int returnSize;
    int *returnColumnSizes;
    char ***groups = groupAnagrams(strs, strsSize, &returnSize, &returnColumnSizes);

    printf("Grouped Anagrams:\n");
    for (int i = 0; i < returnSize; i++)
    {
        printf("[");
        for (int j = 0; j < returnColumnSizes[i]; j++)
        {
            printf("\"%s\"", groups[i][j]);
            if (j < returnColumnSizes[i] - 1)
                printf(", ");
        }
        printf("]\n");
    }
    free(returnColumnSizes);
    // Free each group's array (already freed in groupAnagrams, so just free the result array)
    free(groups);
    printf(KGRN "Tests passed successfully!\n" KRESET);
    return 0;
}
