"""
採用迴圈版本
"""


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
        previous = None
        # 若兩個 Node 都仍有下一筆 Next
        while((add1.next != None) or (add2.next != None)):
            # 1. 先計算
            sum = (add1.val + add2.val) + carry
            remainder = sum % 10
            carry = (sum) // 10
            # 2. 建立 Node 並指派給前一個 Node 的 Next
            current = ListNode(remainder)
            if head.next is None:
                # 如果還沒有指派過，先從 head.next 開始
                head.next = current
                previous = current
            else:
                previous.next = current
                previous = previous.next

            # 3. 下一位數如果有 next 為空，則建立 0 值的 next 值
            add1 = add1.next if add1.next else ListNode(0)
            add2 = add2.next if add2.next else ListNode(0)

        # 4. 兩個位數皆已經沒有 next，計算最後一位加法
        sum = (add1.val + add2.val) + carry
        remainder = sum % 10
        carry = (sum) // 10
        current = ListNode(remainder)
        # 兩個位數皆已經沒有 next 卻仍可以累加算出 Carry 代表該兩個數值皆為個位數計算才有可能
        # 產生 Carry 的 Node
        if carry != 0:
            next = ListNode(carry)
            current.next = next
        # 串接最後一位數，如果沒有 previous 該是該位數為個位數（因為是 Revsese Order)
        if previous:
            previous.next = current
        else:
            head.next = current
        return head.next
