from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            i = 0
            ps = []
            ori = nums[:]
            while(i < len(nums)):
                j = i
                while(j - 1 >= 0):
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    j -= 1
                sub_ps: List[List[int]] = self.permute(nums[j + 1:])
                for sub_p in sub_ps:
                    sub_p = [nums[j]] + sub_p
                    ps.append(sub_p)
                i += 1
                nums[:] = ori[:]
            return ps
