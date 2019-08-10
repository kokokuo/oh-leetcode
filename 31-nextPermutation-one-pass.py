from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. 由最低位 curr = len(nums) -1 往前尋找遞減 curr -= 1
        2.直到該位數值比高位大 nums[curr - 1] < nums[curr]，且大於 0，紀錄該 curr 的位置
        3. 再次由最低位 move = len(nums) -1 開始往高位尋找 move -= 1 :
            => 因為數值要交換一定是 低位數 > 高位數，所以若 curr 找是比較高位
            => 則比他低位的數值一定是由小到大，因此我們可以從最低的數值開始，因此 move -= 1
        4. 當找出離 nums[curr - 1] 最接近的數值，紀錄 move 值 :
            => nums[curr - 1] < nums[move] 時
        4. 把 nums[curr - 1] 與 nums[move] 交換
        5.交換後再把 curr 到 len(nums) - 1 的數值列整個反轉：
            => 因為此時 nums[curr] 到 nums[len(nums) - 1] 會是一個降序
            => after_nums = nums[curr:]
            => nums[:curr] + after_nums[::-1]
        """
        found = False
        curr = len(nums) - 1
        # print("交換前:", nums)
        while(curr > 0 and nums[curr] <= nums[curr - 1]):
            curr -= 1
        # print("要交換的位置索引:", curr)
        if curr > 0:
            move = len(nums) - 1
            # 找到交換的位置，從先前比較低位數字找尋最接近的數與 curr - 1 的數值替換
            while(curr < move and (nums[curr - 1] >= nums[move])):
                move -= 1
            # 找出比 nums[curr - 1] 大，卻比 nums[curr] 小的數值索引，交換兩數
            # print("move 索引:", move, "-> nums[move]:", nums[move])
            # print("curr - 1 索引:", curr - 1, "-> nums[curr -1]: ", nums[curr - 1])
            nums[move], nums[curr - 1] = nums[curr - 1], nums[move]
            # print("交換後的結果:", nums)
            # 把最高位數後面的數字反轉
            after_nums = nums[curr:]
            # print("數字反轉前半段 nums[:curr]:", nums[:curr], \
            # ", 後半段 nums[curr:] 反轉", after_nums[::-1])
            nums[:] = nums[:curr] + after_nums[::-1]
        else:
            nums[:] = nums[::-1]
        # print("交換後:", nums)
        # print("==================")
