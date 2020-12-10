'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
'''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split(' ')
        return len(set(pattern)) == len(set(str)) == len(set(zip(pattern, str))) and len(pattern) == len(str)
