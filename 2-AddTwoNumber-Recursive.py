"""
遞迴版本在 LeetCode 會超時，所以會改用迴圈版本
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. 先計算
        carry = 0
        addend = l1.val if l1 is not None else 0
        augend = l2.val if l2 is not None else 0
        sum = (addend + augend) % 10
        carry = (addend + augend) // 10
        # 2. 檢查兩個 Node 是否還有 Next
        if (l1.next is not None) or (l2.next is not None):
            # 3. 遞迴下一位數，如果有 next 為空，則建立 0 值的 next 值
            next_addend = l2.next if l2.next else ListNode(0)
            next_augend = l1.next if l1.next else ListNode(0)
            next_sum = self.addTwoNumbers(next_addend, next_augend)
            # 取回下一位數的計算後做 Carry 累加，若進位，則再次遞迴
            if next_sum.val + carry >= 0:
                next_sum = self.addTwoNumbers(next_sum, ListNode(carry))
            else:
                next_sum.val += carry
            # 跳至外層串接 NextNode下一位數
        else:
            # 皆沒有 Node，表示皆到最後一個 Node
            # 若無 Carry 有值，直接建立累加的 Node 值回傳
            if carry == 0:
                return ListNode(sum)
            else:
                # 若有 Carry 建立 Carry 的 NextNode，跳至外層串接 NextNode下一位數
                next_sum = ListNode(carry)
        # 回到外層串接 NextNode 下一位數
        # (遞迴後的 NextNode 或到最後一位數的 NextCode 都會執行此段)
        current_node = ListNode(sum)
        current_node.next = next_sum
        return current_node
