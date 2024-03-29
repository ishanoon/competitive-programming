"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.



Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"

"""


def find_the_difference(s: str, t: str):
    s_times = {}
    t_times = {}

    for char in s:
        s_times[char] = s_times.get(char, 0) + 1
    for char in t:
        t_times[char] = t_times.get(char, 0) + 1

    for char in t_times:
        if char not in s_times or t_times[char] > s_times[char]:
            return char


print(find_the_difference("", "y"))
print(find_the_difference("abcd", "abcde"))
