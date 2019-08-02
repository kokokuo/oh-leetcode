from typing import List


class Solution:
    """
    聰明的作法：透過數學集合計算
    LeetCode 的方式：https://leetcode.com/problems/single-number/solution/
    """
    def singleNumber(self, nums: List[int]) -> int:
        """
        集合算法，透過集合抓取每一個數字後對總和在乘上 2 表示如果都是雙數的總和
        再扣掉傳入事實上的結果值，最後的差就會是單數的數字
        在 LeetCode 尚有一個更猛的作法透過 XOR 運算...
        """
        return 2 * sum(set(nums)) - sum(nums)
