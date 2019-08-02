from typing import List


class Solution:
    def isValid(self, src: str) -> bool:
        """
        檢查輸入的括號符號是否有匹配
        1. 先檢查是否為奇數長度，若為奇數則不匹配
        2. 尋訪給一個字元，若 Stack 長度為 0 先放入候選符號字元
        3. 若 Stack 不為 0 ，則把放置在裡面的候選符號字元 Pop 出來與當下的符號字元匹配
        4. 若有匹配表示該符號為一組，若不匹配，把拿出來的候選符號與此次的符號字元都放入
        5. 到下一次回圈在 Pop 出最上面的候選符號再次匹配
        """
        valid_times = 0
        candidate_stack: List = []
        brackets_types = ["()", "{}", "[]"]
        if len(src) % 2 != 0:
            return False
        for idx, char in enumerate(src):
            if len(candidate_stack) != 0:
                candidate = candidate_stack.pop()
                if candidate + char in brackets_types:
                    valid_times += 1
                else:
                    candidate_stack.append(candidate)
                    candidate_stack.append(char)
            else:
                candidate_stack.append(char)
        if valid_times == (len(src) // 2):
            return True
        return False
