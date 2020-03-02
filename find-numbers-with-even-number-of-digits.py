"""
Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
"""

import math
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # count = 0
        # for number in nums:
        #     digits = 0
        #     while True:
        #         number /= 10
        #         if number < 0.1:
        #             break
        #         else:
        #             digits += 1
        #     count += 0 if digits % 2 else 1
        # return count
        count = 0
        for number in nums:
            count += 0 if (int(math.log10(number)) + 1) % 2 else 1
        return count


nums = [12, 345, 2, 6, 7896]
Output = Solution().findNumbers(nums)
print(Output)
