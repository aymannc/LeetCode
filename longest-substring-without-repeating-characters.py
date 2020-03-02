"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""


def length_of_longest_substring(s: str) -> int:
    dic = dict()
    max_sec = 0
    sub_str = ""
    for c in s:
        try:
            if dic[c] == 1:
                sub_str = ""
                dic = dict()
        except:
            dic[c] = 1
            sub_str += c
        if max_sec < len(sub_str):
            max_sec = len(sub_str)
    return max_sec


Input = "aab"
print(length_of_longest_substring(Input))
