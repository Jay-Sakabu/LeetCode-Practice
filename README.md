# LeetCode Practice

This repository contains solutions to practice problems from [LeetCode](https://leetcode.com/), focusing on data structures and algorithms. Most solutions will be implemented in Python, with occasional solutions also made in C and Java.

## Why Multiple Languages?

Python is used because it allows for a quick and relatively simple route for solving problems. Its rich library and native support for complex data types make it hassle-free to manipulate and transform data as needed. With abstract data types included out of the box, it's no wonder why Python is a go-to language for many developers.

C, on the other hand, requires more deliberate design (especially for more complex problems). It lacks many of Python's built-in convenient functionality. To illustrate, if you want to implement a hash map you need to set up a `struct` yourself, and much of the implementation is dependent on you as the developer [such as with this implementation](https://stackoverflow.com/questions/53217476/hashmap-implementation-problem-in-c-with-void-pointer-as-value).

```C
struct node{
    char * key;
    void * value; // We use a void pointer here so that we can use any data type for 'value'. 
                  // Requires manual typecasting to prevent bugs!
};
```

On the other hand, Python provides native support in the form of [Python Dictionaries!](https://www.w3schools.com/python/python_dictionaries.asp)

```Python
my_dictionary = {}
my_dictionary["example"] = 42 # This could be a string, True/False, float, and it would work!
                              # No manual casting or type checking needed!

print(f"Value for 'example': {my_dictionary['example']}") #Prints value of 'example': 42
```

As a result, programming in C requires developers to think more deeply and intentionally about data handling, making it a valuable learning tool.

## Contents

- Data structures (arrays, linked lists, trees, etc.)
- Algorithms (sorting, searching, dynamic programming, etc.)
- Well-commented code for learning and reference

## Purpose

To improve problem-solving skills and deepen understanding of core Python, Java, and C functionality while also familiarizing myself with more complex data-structures and algorithms.
