"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
"""
import random
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        sum = random.randint(-n, n)
        results = [sum]
        for i in range(1, n - 1):
            if sum > 0:
                min, max = -n, 0
            else:
                min, max = 0, n
            while True:
                number = random.randint(min, max)
                if number not in results:
                    break
            sum += number
            results.append(number)
        results.append(-sum)
        return results
        # return list(range(1-n,n,2))


list = Solution().sumZero(7)
print(list)
print(sum(list))
