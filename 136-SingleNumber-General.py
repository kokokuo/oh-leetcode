from typing import List


class Solution:
    """
    大多數人的類似作法：Big-O 為 O(N ** 2)
    先尋訪然後又用 if in 尋訪一次找碴有無出現該 Key，而且空複雜度為 O(N)
    LeetCode 的方式：https://leetcode.com/problems/single-number/solution/
    """
    def singleNumber(self, nums: List[int]) -> int:
        pool: List = []
        for num in nums:
            if num not in pool:
                pool.append(num)
            else:
                pool.remove(num)
        if len(pool) == 0:
            return 0
        return pool.pop()
        