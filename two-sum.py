from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for e, number in enumerate(nums):
        comp = target - number
        if comp in dic:
            return [dic[comp], e]
        else:
            dic[number] = e


Input = [2, 7, 11, 15]
target = 9
print(two_sum(Input, target))
