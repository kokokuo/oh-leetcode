from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        拿 target 減去 val 的 remaining 放入字典中，下次尋訪便可以先直接找字典有無匹配。
        若無匹配，則再次拿輸入的 target 減去當下 val 取得 remaining 再次放入字典中，
        作為新的可能結果，並持續尋找。
        """
        found: Dict = {}
        for i, val in enumerate(nums):
            if val in found.keys():
                indexes = [found[val], i]
                return indexes
            else:
                remaining = target - val
                found[remaining] = i
        return []
