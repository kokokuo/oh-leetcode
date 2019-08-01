

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        add1 = l1
        add2 = l2
        # 建立一個起始的 Head 與 一個指向為前一個紀錄的 Node
        head = ListNode(0)
        previous = head
        # 若兩個 Node 都有資料
        while(add1 or add2):
            # 1. 先計算
            val1 = add1.val if add1 else 0
            val2 = add2.val if add2 else 0
            sum = (val1 + val2) + carry
            remainder = sum % 10
            carry = (sum) // 10
            # 2. 建立 Node 並指派給前一個 Node 的 Next
            current = ListNode(remainder)
            previous.next = current
            previous = previous.next
            # 3. 把下一個位數替換成自己
            if add1:
                add1 = add1.next
            if add2:
                add2 = add2.next
        # 兩個位數皆已經沒有 next 卻仍可以累加算出 Carry 代表該兩個數值為最高位數
        # 產生 Carry 的 Node
        if carry > 0:
            previous.next = ListNode(carry)
        return head.next
